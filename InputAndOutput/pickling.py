import pickle

# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"),
#     (2, "Psycho"),
#     (3, "Mayhem"),
#     (4, "Kentish Tom Waltz")
# )
#
# with open("imelda.pickle", "bw") as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open("imelda.pickle", "br") as imelda_pickle:
#     imelda_2 = pickle.load(imelda_pickle)
#
# print(imelda_2)

# imelda = "More Mayhem", "Imelda MAy", "2011", (
#     (1, "Pulling the Rug"),
#     (2, "Psycho"),
#     (3, "Mayhem"),
#     (4, "Kentish Tom Waltz")
# )
#
# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# number = 323414423
#
# with open("imelda.pickle", "bw") as pickle_file:
#     pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even, pickle_file, protocol=0)
#     pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#     pickle.dump(number, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
#
# with open("imelda.pickle", "br") as pickle_file:
#     album2 = pickle.load(pickle_file)
#     even2 = pickle.load(pickle_file)
#     odd2 = pickle.load(pickle_file)
#     number2 = pickle.load(pickle_file)
#
# print(album2)
# print(even2)
# print(odd2)
# print(number2)

pickle.loads(b"cos\nsystem\n(S' del imelda.pickle'\nR.")  # For Win
