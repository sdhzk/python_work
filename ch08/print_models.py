# unprint_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprint_designs:
#     current_design = unprint_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for complated_model in completed_models:
#     print(complated_model)

def print_models(unprint_designs, completed_models):
    while unprint_designs:
        current_design = unprint_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprint_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprint_designs[:], completed_models)
show_completed_models(completed_models)