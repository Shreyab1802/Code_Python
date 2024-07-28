# You are given N recipes, the K-th of which is represented by a string A[KI. Each letter of the string represents a single unit of an ingredient: for example, recipe "toast" requires two units of ingredie
# 't' and one unit of ingredients 'o, 'a' and's.
# You are also given a list of available ingredients represented by a string S. Which recipes
# can be prepared using ingredients from the list?
# Write a function:
# class Solution { public int solution(Stringil A, String S); }
# that, given an array A consisting of N strings representing the recipes, and a string S representing
# the list of available ingredients, returns the number of recipes that can be prepared using available ingredients.
# Examples:
# 1. Given A = ['toast", "bread", "breada", "cheese"] and S = "abcdeeehrs", the function should return 2.
# With our ingredients, recipes "bread" and "cheese" can be prepared (note thot it is not necessary to
#               create both at the same time). We cannot prepare "toast" as some ingredients are missing
#     (for example 't), and there are not enough units of 'a' to prepare "breada".
# 2. Given A = l"az", "azz", "zza", "zzz", "zzzz"] and S = "azzz", the function should return 4. With our
# ingredients, we can prepare "az", "azz", "zza" and "zzz".
# Assume that:
# • N is an integer within the range [1..100);
# • the length of string S is within the range [0..100);
# • the length of every string in array A is within the range [1..100];
# • the elements of A are all distinct;
# • string S and every string in array A consist only of lowercase letters (a-
# In your solution, focus on correctness. The performance of your solution will not be the focus of the

def solution(A, S):
    count = 0
    temp = S + ' '
    for recipe in A:
        can_prepare = True
        print('for' + recipe)
        print(temp)
        S = temp.strip()
        print(S)
        for ingredient in recipe:
            if ingredient not in S:
                can_prepare = False
                break
            else:
                ingredientIndex = S.index(ingredient)
                print('index for' + ingredient)
                print('index')
                S = S[:ingredientIndex] + S[ingredientIndex + 1:]
                print('removing '+ ingredient)
                print(S)
        if can_prepare:
            print(recipe)
            count += 1
        print('run finish for' + recipe)
    return count


S = 'abcdeeehsrs'
print(solution(['toast', 'bread', 'breada', 'cheese'], S))
