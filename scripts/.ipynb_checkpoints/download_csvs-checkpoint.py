import flywheel
import os

csvs_dir = 'csvs'

fw = flywheel.Client()
project = fw.lookup('davis/presurgicalEpilepsy')
analyses = fw.get_analyses("projects", project.id, "all")
scenemem_analyses = [a for a in analyses if '2020-8-27_WT_scenemem' in a.label]

for analysis in scenemem_analyses:
    file = [f for f in analysis.files if "scenemem" in f.name]
    if len(file) < 1:
        sub = fw.get(analysis.parents['subject'])
        print("{}: scenemem csv not found.".format(sub.label))
        continue
    analysis.download_file(file[0].name, os.path.join(csvs_dir, file[0].name))
