import flywheel
import os

bold_dir = 'maps'

fw = flywheel.Client()
project = fw.lookup('davis/presurgicalEpilepsy')
analyses = fw.get_analyses("projects", project.id, "all")
fprep_analyses = [a for a in analyses if 'linguamap' in a.label and 'scenemem' in a.label]

for analysis in fprep_analyses:
    sub_label = fw.get(analysis.parents['subject']).label
#     if sub_label != 'P091':
#         continue
    ses_label = fw.get(analysis.parents['session']).label
    # subdir = os.path.join(bold_dir, sub_label)
    # os.makedirs(subdir, exist_ok=True)
    analysis_id = analysis.id
    print("ANALYSIS ID: " + analysis_id)

    if analysis.files is None:
        continue

    # get zip file
    zip_files = [f for f in analysis.files if "report_results" in f.name and 'zip' in f.name]
    if len(zip_files) < 1:
        continue
    print(zip_files[0].name)
    if len(zip_files) > 0:
        zip_info = analysis.get_file_zip_info(zip_files[0].name)
        #print(zip_info)
        new_sub_label = sub_label.replace('0', '')
        print(new_sub_label)
        try:
            analysis.download_file_zip_member(zip_files[0].name, \
            'sub-{}_report_results/scenemem/scenemem_fdr_thresholded_z_resample.nii.gz'.format(sub_label), \
            os.path.join(bold_dir, sub_label+'_fdr_thresholded_z.nii.gz'))
            print("Downloading from " + sub_label)
        except Exception as e:
            print(e)
            print(sub_label)
        # try:
        #     analysis.download_file_zip_member(zip_files[0].name, \
        #     '{}/fmriprep/sub-{}/ses-{}/func/sub-{}_ses-{}_task-scenemem_*.nii.gz'.format(analysis_id, sub_label,ses_label, sub_label,ses_label), \
        #     os.path.join(subdir, sub_label+'_preproc_bold.nii.gz'))
        #     print("DOWNLOADED " + sub_label)
        # except Exception as e:
        #     print(e)
        #     print(sub_label)
