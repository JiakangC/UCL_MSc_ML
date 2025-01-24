#%%
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from random import randrange
import collections
from collections import Counter
import seaborn as sns
#%%
# load data
message  = open('message.txt','r').read().replace('\n', '')
symbols = open('symbols.txt','r').read().replace('\n', '')
war_and_peace = open('2600-0.txt','r').read().replace('\n', '').lower()
# we use war and peace as proposal. In that case, this text need to be clean. 
# By going through the text, we found the name in text like 'Bolkónskaya' influence, we replace them with regular letter
war_and_peace.replace('á', 'a')
war_and_peace.replace('á', 'a')
war_and_peace.replace('é', 'e')
war_and_peace.replace('ú', 'u')
war_and_peace.replace('á', 'a')
war_and_peace.replace('í', 'i')
war_and_peace.replace('ó', 'o')
war_and_peace.replace('ç', 'c')
war_and_peace.replace('ë', 'e')
war_and_peace.replace('ë', 'e')
war_and_peace.replace('“', '"')
war_and_peace.replace('”', '"')
war_and_peace.replace('‘', "'")
war_and_peace.replace('’', "'")
special_ch = ['~','@','#','$','%','^','&','_']
for i in special_ch:
    war_and_peace = war_and_peace.replace(i, '')
space_list = ['  ','   ','    ','     ','      ']
for j in space_list:
    war_and_peace = war_and_peace.replace(i, ' ')

# %%
# Q5 (c) 
# Transition Matrix Psi(alpha|beta)
def Psi(text, symbols):
    num_text = len(text)
    # numbers of symbols
    num_sym = len(symbols)
    # initial the counts
    transition_counts = np.zeros((num_sym,num_sym))
    # go through text
    for i in range(num_text):
        # pick the character
        current_sym = text[i-1] # beta
        next_sym = text[i] # alpha
        # check whether these character in the symbols. 
        # if character within symbols, we get id. Otherwise, return -1
        current_sym_id = symbols.find(current_sym)
        next_sym_id = symbols.find(next_sym)       
        if (current_sym_id != -1) and (next_sym_id != -1):
            transition_counts[current_sym_id, next_sym_id] += 1
        else:
            continue
    # normalize 
    row_sums = np.sum(transition_counts, axis=1).reshape(-1, 1)
    Psi = np.divide(transition_counts, row_sums, where=row_sums != 0)
    return Psi

transition_matrix = Psi(war_and_peace, symbols)
# %% 
plt.figure(figsize=(25,25))
sns.heatmap(np.round(transition_matrix,2),annot=True, xticklabels=True,yticklabels=True, square=True, cmap="coolwarm").get_figure
plt.savefig('Q5(a).png')
# %%


# %%
# Q5 (c) 

def decrypt_message(text, symbols, key):
    # sigma inverse (e)
    # decode the key to symbols
    decoded_message=str()
    for i in text:
        index = list(key).index(i)
        letter = symbols[index]
        decoded_message+=letter
    return decoded_message

def Proposal(key):
    # Select two distinct indices to swap
    key_new = key.copy()
    idx1, idx2 = random.sample(range(len(key)), 2)
    
    # Swap the characters at these indices
    key_new[idx1], key_new[idx2] = key[idx2], key[idx1]

    return key_new

def log_likelihood_function(text, symbols, key, matrix):
    decoded_message =  decrypt_message(text, symbols, key)
    log_likelihood = 0
    for i in range(1,len(text)):
        beta = decoded_message[i-1]
        alpha = decoded_message[i]
        beta_id = symbols.index(beta)
        alpha_id = symbols.index(alpha)
        log_likelihood += np.log(matrix[beta_id, alpha_id])
    return log_likelihood


def MCMC_MH(symbols, text, matrix, intelligent_guess, iterations=10000):
    key =  intelligent_guess.copy() 
    log_likelihoods = []
    for i in range(iterations):
        proposal_key = Proposal(key).copy()
        current_prob = log_likelihood_function(text, symbols, key, matrix)
        proposal_prob = log_likelihood_function(text, symbols, proposal_key, matrix)
        log_accept_ratio = proposal_prob - current_prob
        u = np.log(np.random.rand())
        if u < log_accept_ratio:
            key = proposal_key.copy()  
        # print every 100 iteration
        if i % 100 == 0:
            print('Iteration', i, ': \n', decrypt_message(text, symbols, key)[:60])
            print(current_prob)
            log_likelihoods.append(current_prob)          
    return key, log_likelihoods
# %%
def count_and_rank_characters(message, symbols):
    # count each character in the message
    char_count = Counter(message)
    
    # rank characters by frequency, with the most common characters first
    ranked_chars = [char for char, _ in char_count.most_common()]
    
    # create an ordered list of symbols based on the ranked characters
    ordered_symbols = []
    seen_symbols = set()
    
    # First, add symbols that match the ranked characters
    for char in ranked_chars:
        if char in symbols:
            ordered_symbols.append(char)
            seen_symbols.add(char)
    
    # get the remaining symbols that were not in the ranked characters
    remaining_symbols = [char for char in symbols if char not in seen_symbols]
    
    # shuffle the remaining symbols randomly and add to the ordered list
    random.shuffle(remaining_symbols)
    ordered_symbols.extend(remaining_symbols)
    
    return ordered_symbols

def combined_mapping_functions(list1, list2, original):

    # map list1 elements to unique numbers (their index)
    number_mapping = {element: index for index, element in enumerate(list1)}
    
    # map list1 to list2 if they have the same length
    if len(list1) != len(list2):
        raise ValueError("list1 and list2 must have the same length.")
    shuffled_map = {list1[i]: list2[i] for i in range(len(list1))}
    
    # reorder shuffled_map to match the order of original
    reordered_map = {key: shuffled_map[key] for key in original if key in shuffled_map}
    
    # return the reorder values
    return reordered_map.values()
#%%
r1 = count_and_rank_characters(war_and_peace, symbols)
r2 = count_and_rank_characters(message, symbols)
transition_matrix = Psi(war_and_peace, symbols) + 0.001
intelligent_guess = combined_mapping_functions(r1, r2, list(symbols))
decrypt_key, log_values = MCMC_MH(symbols, message, transition_matrix, list(intelligent_guess), iterations=10000)
# %%
x = np.linspace(0,10000,100)
plt.grid()
plt.xlabel("Iterations")
plt.ylabel("Log-likelihood")
plt.title("Log-likelihood vs Iterations")
plt.plot(x, log_values)
plt.savefig('Q5(d).png')
# %%
