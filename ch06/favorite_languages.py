# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }
# print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}")

# print(favorite_languages.get('lee', 'No language value assigned.'))

# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages:
#     print(name.title())

# for name in sorted(favorite_languages.keys()):
#     print(name.title())

# for language in favorite_languages.values():
#     print(language.title())

# for language in set(favorite_languages.values()):
#     print(language.title())

# languages={'python','java','c','python'}
# print(languages)

favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['rust','go'],
    'phil': ['python','hackell'],
}
for name,languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language are: {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite language are:")
        for language in languages:
            print(f'\t{language.title()}')