# Matn faylini ochish
with open('matn.txt', 'r') as file:
    lines = file.readlines()

# Bo'sh qatorlarni olib tashlash
cleaned_lines = [line.strip() for line in lines if line.strip()]

# Natijani saqlash
with open('matn_new.txt', 'w') as file:
    file.write('\n'.join(cleaned_lines))
