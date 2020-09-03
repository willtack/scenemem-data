import flywheel
import os

bold_dir = '/home/will/Repositories/language-data/scenemem/preprocBold'

fw = flywheel.Client()
project = fw.lookup('davis/presurgicalEpilepsy')
analyses = fw.get_analyses("projects", project.id, "all")
fprep_analyses = [a for a in analyses if '3.4' in a.label or '34' in a.label]

for analysis in fprep_analyses:
    sub_label = fw.get(analysis.parents['subject']).label
    # if sub_label != 'P091':
    #     continue
    ses_label = fw.get(analysis.parents['session']).label
    subdir = os.path.join(bold_dir, sub_label)
    os.makedirs(subdir, exist_ok=True)
    analysis_id = analysis.id
    print("ANALYSIS ID: " + analysis_id)

    if analysis.files is None:
        continue

    # get zip file
    zip_files = [f for f in analysis.files if "fmriprep" in f.name and 'zip' in f.name]
    if len(zip_files) < 1:
        continue
    print(zip_files[0].name)
    if len(zip_files) > 0:
        zip_info = analysis.get_file_zip_info(zip_files[0].name)
        print(zip_info)
        # try:
        #     analysis.download_file_zip_member(zip_files[0].name, \
        #     '{}/fmriprep/sub-{}/ses-{}/func/sub-{}_ses-{}_task-scenemem_run-01_space-T1w_desc-preproc_bold.nii.gz'.format(analysis_id, sub_label,ses_label, sub_label,ses_label), \
        #     os.path.join(subdir, sub_label+'_preproc_bold.nii.gz'))
        #     print("Downloading from " + sub.label)
        # except Exception as e:
        #     print(e)
        #     print(sub_label)
        # try:
        #     analysis.download_file_zip_member(zip_files[0].name, \
        #     '{}/fmriprep/sub-{}/ses-{}/func/sub-{}_ses-{}_task-scenemem_*.nii.gz'.format(analysis_id, sub_label,ses_label, sub_label,ses_label), \
        #     os.path.join(subdir, sub_label+'_preproc_bold.nii.gz'))
        #     print("DOWNLOADED " + sub_label)
        # except Exception as e:
        #     print(e)
        #     print(sub_label)
