# to check if list is subset of other
# using issubset()
#a)the truth value of B ⊆ A

A = list(input("enter the element of list A:"))
B = list(input("enter the element of list B:"))

# printing original lists12
print("Original list A : " + str(A))
print("Original sub list B : " + str(B))

# using issubset() to
# check subset of list
flag = 0
if not set(B).issubset(set(A)):
    pass
else:
    flag = 1

if not flag:
    print("FALSE, B is not a subset of A.")
# printing result
else:
    print("TRUE, B is a subset of A .")

#b) the set A-B
    print("the setA-B:", (set(A)-set(B)))

#c) the set A × B
    crossproduct =[[i, j]for i in A for j in B]
    print("the set A × B:", crossproduct )



