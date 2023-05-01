s = input()

if s in ["Flask", "Django", "Fast-API"]:
    print(f"Python({s}),Backend-dev")
elif s in ["Angular", "React", "Vue"]:
    print(f"JavaScript/TypeScript({s}),Frontend-dev")
elif s in ["Flutter", "React Native"]:
    print(f"JavaScript({s}),Cross-Mobile-dev")
elif s in ["Pandas", "skit-learn", "keras"]:
    print(f"Python({s}),Data-Scientist")
else:
    print("модель еще не обучена")
