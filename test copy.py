from datumaro.cli.__main__ import main

# main(['project', 'export', '-o', 'D:\\새 폴더\\projects\\..\\export\\새 폴더_merge_cvat',
      # '-p', 'D:\\새 폴더\\projects\\새 폴더_merge', 
      # '-f', 'cvat', "--overwrite", '--', '--save-images'])
# main(['project', 'export', '-o', 'D:\\새 폴더\\export/task_20.09.25 dw02-1 human_dh_0922 _dh_a dh_a1124-1129_t24-2021_02_10_10_45_08-cvat for images 1.1_coco/',
#       '-p', 'D:\\새 폴더\\projects\\task_20.09.25 dw02-1 human_dh_0922 _dh_a dh_a1124-1129_t24-2021_02_10_10_45_08-cvat for images 1.1', 
#       '-f', 'cvat', "--overwrite", '--', '--save-images'])
# main(['merge', 'D:\\새 폴더\\projects\\task_20.09.25 dw02-1 human_dh_0922 _dh_a dh_a1124-1129_t24-2021_02_10_10_45_08-cvat for images 1.1/',
#       'D:\\새 폴더\\projects\\task_20.09.28 dw02-2 human_nh_0928 _cmr-a nh_p1209-1204_t28-2021_02_03_16_08_01-cvat for images 1.1/',
#       'd:\\새 폴더/projects/task_test-2021_01_21_14_17_34-cvat for images 1.1/'])
main(['project', 'export', '-o', 'D:\\새 폴더/export/새 폴더_merge_cvat/',
      '-p', 'D:\\datumaro/merged/', 
      '-f', 'coco', "--overwrite", '--', '--save-images'])