"""Copy the normalised assets into town/a/ with the flat names the town page expects."""
import glob, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
N = os.path.join(HERE, '..', 'assets', 'normalized')
D = os.path.join(HERE, '..', 'town', 'a')
os.makedirs(D, exist_ok=True)
def cp(src, dst):
    shutil.copy(os.path.join(N, src), os.path.join(D, dst))
for f in glob.glob(N + '/ground/bank_recolored/*.png'): cp(os.path.relpath(f, N), 'bank_' + os.path.basename(f))
for f in glob.glob(N + '/ground/shore/*.png'): cp(os.path.relpath(f, N), 'shore_' + os.path.basename(f))
for f in glob.glob(N + '/ground/path/*.png'): cp(os.path.relpath(f, N), 'path_' + os.path.basename(f))
for f in glob.glob(N + '/ground/variation_fixed/*.png'): cp(os.path.relpath(f, N), 'var_' + os.path.basename(f))
for i in (1, 2, 3): cp(f'ground/grass{i}.png', f'grass{i}.png')
for sub in ('trees_species', 'trees_stages', 'trees_evergreen_blossom', 'plants_rocks', 'water_plants'):
    for f in glob.glob(f'{N}/nature/{sub}/*.png'): cp(os.path.relpath(f, N), 'n_' + os.path.basename(f))
for sub in ('town_a', 'town_b'):
    for f in glob.glob(f'{N}/props/{sub}/*.png'): cp(os.path.relpath(f, N), 'p_' + os.path.basename(f))
for a, b in [('stories_cut', 'b_tower'), ('glasshouse_cut', 'b_glass'), ('markethall_cut', 'b_market'), ('aboutme_cut', 'b_cabin'), ('mill_construction_cut', 'b_mill')]:
    cp(f'buildings/{a}.png', b + '.png')
cp('characters/traveller_final/sheet_4dir.png', 'trav.png')
cp('characters/traveller_final/sheet_idle.png', 'idle.png')
print(len(os.listdir(D)), 'files in', D)
