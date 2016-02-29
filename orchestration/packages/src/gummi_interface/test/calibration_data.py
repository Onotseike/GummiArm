#!/usr/bin/env python

alphasFlexor = [1.356, 1.635, 1.884, 2.103, 2.278, 2.425, 2.566, 2.698, 2.852, 3.017, 3.152, 3.293,
                3.398, 3.513, 3.662, 3.798, 3.91, 1.466, 1.644, 1.824, 1.968, 2.103, 2.247, 2.396,
                2.539, 2.688, 2.844, 2.996, 3.146, 3.264, 3.402, 3.531, 3.649, 3.789, 1.281, 1.456,
                1.626, 1.781, 1.925, 2.077, 2.21, 2.362, 2.502, 2.657, 2.824, 2.981, 3.112, 3.246,
                3.385, 3.508, 3.629, 1.077, 1.255, 1.416, 1.582, 1.723, 1.868, 2.011, 2.168, 2.309,
                2.462, 2.629, 2.764, 2.918, 3.051, 3.208, 3.224, 3.224, 1.649, 1.827, 1.983, 2.141,
                2.275, 2.424, 2.566, 2.726, 2.87, 3.014, 3.157, 3.3, 3.412, 3.527, 3.692, 3.81,
                3.932, 1.563, 1.75, 1.902, 2.054, 2.192, 2.344, 2.493, 2.637, 2.773, 2.93, 3.08,
                3.217, 3.352, 3.468, 3.608, 3.732, 3.85, 1.45, 1.637, 1.796, 1.951, 2.086, 2.229,
                2.376, 2.531, 2.668, 2.832, 2.977, 3.119, 3.247, 3.366, 3.53, 3.648, 3.763, 1.327,
                1.502, 1.674, 1.832, 1.977, 2.121, 2.264, 2.407, 2.559, 2.7, 2.878, 3.02, 3.145,
                3.287, 3.419, 3.542, 3.669, 1.752, 1.921, 2.075, 2.223, 2.365, 2.519, 2.666, 2.803,
                2.958, 3.088, 3.231, 3.364, 3.513, 3.616, 3.734, 3.859, 3.998]

alphasExtensor = [1.666, 1.666, 1.666, 1.666, 1.621, 1.47, 1.324, 1.178, 1.034, 0.891, 0.739, 0.606,
                  0.471, 0.383, 0.229, 0.097, -0.035, 1.692, 1.499, 1.327, 1.172, 1.039, 0.891, 0.759,
                  0.595, 0.459, 0.302, 0.14, -0.002, -0.13, -0.261, -0.371, -0.494, -0.641, 1.132,
                  0.945, 0.775, 0.612, 0.466, 0.321, 0.193, 0.028, -0.106, -0.258, -0.426, -0.584,
                  -0.715, -0.844, -0.982, -1.095, -1.243, 0.69, 0.5, 0.337, 0.176, 0.029, -0.112,
                  -0.262, -0.419, -0.558, -0.709, -0.876, -1.022, -1.166, -1.282, -1.44, -2.505, -3.043,
                  2.269, 2.072, 1.914, 1.756, 1.621, 1.474, 1.331, 1.177, 1.032, 0.882, 0.752, 0.603,
                  0.472, 0.383, 0.192, 0.089, -0.035, 1.924, 1.724, 1.568, 1.411, 1.276, 1.141, 0.979,
                  0.848, 0.699, 0.535, 0.396, 0.241, 0.11, -0.006, -0.147, -0.262, -0.357, 1.566,
                  1.368, 1.203, 1.048, 0.908, 0.769, 0.627, 0.466, 0.328, 0.167, 0.034, -0.13, -0.255,
                  -0.348, -0.537, -0.65, -0.782, 1.216, 1.023, 0.853, 0.692, 0.568, 0.403, 0.265,
                  0.11, -0.035, -0.187, -0.342, -0.5, -0.624, -0.759, -0.882, -1.003, -1.158, 2.395,
                  2.206, 2.051, 1.891, 1.756, 1.609, 1.463, 1.312, 1.169, 1.032, 0.885, 0.742, 0.632,
                  0.494, 0.347, 0.27, 0.137]

thetas = [-0.481, -0.419, -0.358, -0.291, -0.235, -0.174, -0.118, -0.061, 0.0, 0.066, 0.123,
          0.189, 0.24, 0.302, 0.363, 0.424, 0.481, -0.481, -0.419, -0.358, -0.302, -0.24,
          -0.179, -0.118, -0.061, 0.0, 0.061, 0.123, 0.184, 0.24, 0.302, 0.363, 0.424, 0.486,
          -0.481, -0.419, -0.358, -0.302, -0.24, -0.179, -0.118, -0.061, 0.0, 0.061, 0.123,
          0.179, 0.24, 0.302, 0.363, 0.424, 0.481, -0.481, -0.419, -0.358, -0.302, -0.24,
          -0.179, -0.123, -0.061, 0.0, 0.061, 0.123, 0.179, 0.24, 0.302, 0.363, 0.389, 0.389,
          -0.481, -0.419, -0.358, -0.297, -0.24, -0.179, -0.118, -0.056, 0.0, 0.061, 0.123,
          0.184, 0.24, 0.291, 0.368, 0.424, 0.486, -0.481, -0.419, -0.358, -0.302, -0.24,
          -0.174, -0.118, -0.056, 0.0, 0.061, 0.123, 0.179, 0.24, 0.302, 0.363, 0.424, 0.486,
          -0.481, -0.419, -0.358, -0.297, -0.24, -0.179, -0.118, -0.056, 0.0, 0.061, 0.123,
          0.179, 0.24, 0.302, 0.368, 0.424, 0.481, -0.481, -0.419, -0.358, -0.297, -0.235,
          -0.179, -0.118, -0.061, 0.0, 0.061, 0.123, 0.179, 0.24, 0.302, 0.363, 0.43, 0.481,
          -0.481, -0.419, -0.358, -0.302, -0.24, -0.179, -0.118, -0.061, 0.0, 0.061, 0.123,
          0.179, 0.251, 0.302, 0.358, 0.424, 0.486]

ccs = [0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8,
       0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7,
       0.7, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,
       0.6, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
       0.5, 0.5, 0.5, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4,
       0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3,
       0.3, 0.3, 0.3, 0.3, 0.3, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
       0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
       0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
       0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]