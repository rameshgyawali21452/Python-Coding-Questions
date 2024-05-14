# Remove empty strings from the list of strings ?
# l1 = ['Scientist','Engineer','Doctor',','Pilot']
# Rem_em_str = list(filter(None,l1))
l1 = ['Scientist', 'Engineer', 'Doctor', '', 'Pilot']
Rem_em_str = list(filter(None, l1))
print(Rem_em_str)