import numpy as np

shape_Giluwe = (31, 40)
shape_Borden = (39, 44)

Giluwe_cross = np.zeros(shape_Giluwe)
Giluwe_cross[8:28, 18] = 1
Giluwe_cross[16, 4:36] = 1

Giluwe_tongue = np.zeros(shape_Giluwe)
for i in range(5):
    Giluwe_tongue[5 + i, 14 + i] = 1
    Giluwe_tongue[6 + i, 14 + i] = 1

Giluwe_large_tongue = np.zeros(shape_Giluwe)
for i in range(7):
    Giluwe_large_tongue[5 + i, 14 + i] = 1
    Giluwe_large_tongue[6 + i, 14 + i] = 1

Giluwe_upper_tongue = np.zeros(shape_Giluwe)
for i in range(4):
    Giluwe_upper_tongue[7 + i, 16 + i] = 1
    Giluwe_upper_tongue[7 + i, 17 + i] = 1
    #measurement_mask_Giluwe_upper_tongue[7 + i, 18 + i] = 1

Borden_horizontal = np.zeros(shape_Borden)
Borden_horizontal[14, 10:27] = 1
Borden_horizontal[20, 10:27] = 1

Borden_horizontal2 = np.zeros(shape_Borden)
Borden_horizontal2[14, 10:27] = 1
Borden_horizontal2[19, 10:27] = 1