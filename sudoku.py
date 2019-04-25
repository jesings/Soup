#! /usr/bin/python3
import sys
backtracks = 0
cliquemap = {0: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 9, 18, 27, 36, 45, 54, 63, 72], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 1: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 10, 19, 28, 37, 46, 55, 64, 73], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 2: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [2, 11, 20, 29, 38, 47, 56, 65, 74], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 3: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [3, 12, 21, 30, 39, 48, 57, 66, 75], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 4: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [4, 13, 22, 31, 40, 49, 58, 67, 76], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 5: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [5, 14, 23, 32, 41, 50, 59, 68, 77], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 6: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [6, 15, 24, 33, 42, 51, 60, 69, 78], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 7: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [7, 16, 25, 34, 43, 52, 61, 70, 79], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 8: [[0, 1, 2, 3, 4, 5, 6, 7, 8], [8, 17, 26, 35, 44, 53, 62, 71, 80], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 9: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [0, 9, 18, 27, 36, 45, 54, 63, 72], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 10: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 10, 19, 28, 37, 46, 55, 64, 73], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 11: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [2, 11, 20, 29, 38, 47, 56, 65, 74], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 12: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [3, 12, 21, 30, 39, 48, 57, 66, 75], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 13: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [4, 13, 22, 31, 40, 49, 58, 67, 76], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 14: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [5, 14, 23, 32, 41, 50, 59, 68, 77], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 15: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [6, 15, 24, 33, 42, 51, 60, 69, 78], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 16: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [7, 16, 25, 34, 43, 52, 61, 70, 79], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 17: [[9, 10, 11, 12, 13, 14, 15, 16, 17], [8, 17, 26, 35, 44, 53, 62, 71, 80], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 18: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [0, 9, 18, 27, 36, 45, 54, 63, 72], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 19: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [1, 10, 19, 28, 37, 46, 55, 64, 73], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 20: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [2, 11, 20, 29, 38, 47, 56, 65, 74], [0, 1, 2, 9, 10, 11, 18, 19, 20]], 21: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [3, 12, 21, 30, 39, 48, 57, 66, 75], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 22: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [4, 13, 22, 31, 40, 49, 58, 67, 76], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 23: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [5, 14, 23, 32, 41, 50, 59, 68, 77], [3, 4, 5, 12, 13, 14, 21, 22, 23]], 24: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [6, 15, 24, 33, 42, 51, 60, 69, 78], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 25: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [7, 16, 25, 34, 43, 52, 61, 70, 79], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 26: [[18, 19, 20, 21, 22, 23, 24, 25, 26], [8, 17, 26, 35, 44, 53, 62, 71, 80], [6, 7, 8, 15, 16, 17, 24, 25, 26]], 27: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [0, 9, 18, 27, 36, 45, 54, 63, 72], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 28: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [1, 10, 19, 28, 37, 46, 55, 64, 73], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 29: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [2, 11, 20, 29, 38, 47, 56, 65, 74], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 30: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [3, 12, 21, 30, 39, 48, 57, 66, 75], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 31: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [4, 13, 22, 31, 40, 49, 58, 67, 76], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 32: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [5, 14, 23, 32, 41, 50, 59, 68, 77], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 33: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [6, 15, 24, 33, 42, 51, 60, 69, 78], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 34: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [7, 16, 25, 34, 43, 52, 61, 70, 79], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 35: [[27, 28, 29, 30, 31, 32, 33, 34, 35], [8, 17, 26, 35, 44, 53, 62, 71, 80], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 36: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [0, 9, 18, 27, 36, 45, 54, 63, 72], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 37: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [1, 10, 19, 28, 37, 46, 55, 64, 73], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 38: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [2, 11, 20, 29, 38, 47, 56, 65, 74], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 39: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [3, 12, 21, 30, 39, 48, 57, 66, 75], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 40: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [4, 13, 22, 31, 40, 49, 58, 67, 76], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 41: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [5, 14, 23, 32, 41, 50, 59, 68, 77], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 42: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [6, 15, 24, 33, 42, 51, 60, 69, 78], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 43: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [7, 16, 25, 34, 43, 52, 61, 70, 79], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 44: [[36, 37, 38, 39, 40, 41, 42, 43, 44], [8, 17, 26, 35, 44, 53, 62, 71, 80], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 45: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [0, 9, 18, 27, 36, 45, 54, 63, 72], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 46: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [1, 10, 19, 28, 37, 46, 55, 64, 73], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 47: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [2, 11, 20, 29, 38, 47, 56, 65, 74], [27, 28, 29, 36, 37, 38, 45, 46, 47]], 48: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [3, 12, 21, 30, 39, 48, 57, 66, 75], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 49: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [4, 13, 22, 31, 40, 49, 58, 67, 76], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 50: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [5, 14, 23, 32, 41, 50, 59, 68, 77], [30, 31, 32, 39, 40, 41, 48, 49, 50]], 51: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [6, 15, 24, 33, 42, 51, 60, 69, 78], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 52: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [7, 16, 25, 34, 43, 52, 61, 70, 79], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 53: [[45, 46, 47, 48, 49, 50, 51, 52, 53], [8, 17, 26, 35, 44, 53, 62, 71, 80], [33, 34, 35, 42, 43, 44, 51, 52, 53]], 54: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [0, 9, 18, 27, 36, 45, 54, 63, 72], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 55: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [1, 10, 19, 28, 37, 46, 55, 64, 73], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 56: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [2, 11, 20, 29, 38, 47, 56, 65, 74], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 57: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [3, 12, 21, 30, 39, 48, 57, 66, 75], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 58: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [4, 13, 22, 31, 40, 49, 58, 67, 76], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 59: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [5, 14, 23, 32, 41, 50, 59, 68, 77], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 60: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [6, 15, 24, 33, 42, 51, 60, 69, 78], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 61: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [7, 16, 25, 34, 43, 52, 61, 70, 79], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 62: [[54, 55, 56, 57, 58, 59, 60, 61, 62], [8, 17, 26, 35, 44, 53, 62, 71, 80], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 63: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [0, 9, 18, 27, 36, 45, 54, 63, 72], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 64: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [1, 10, 19, 28, 37, 46, 55, 64, 73], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 65: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [2, 11, 20, 29, 38, 47, 56, 65, 74], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 66: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [3, 12, 21, 30, 39, 48, 57, 66, 75], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 67: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [4, 13, 22, 31, 40, 49, 58, 67, 76], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 68: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [5, 14, 23, 32, 41, 50, 59, 68, 77], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 69: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [6, 15, 24, 33, 42, 51, 60, 69, 78], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 70: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [7, 16, 25, 34, 43, 52, 61, 70, 79], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 71: [[63, 64, 65, 66, 67, 68, 69, 70, 71], [8, 17, 26, 35, 44, 53, 62, 71, 80], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 72: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 73: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [1, 10, 19, 28, 37, 46, 55, 64, 73], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 74: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [2, 11, 20, 29, 38, 47, 56, 65, 74], [54, 55, 56, 63, 64, 65, 72, 73, 74]], 75: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [3, 12, 21, 30, 39, 48, 57, 66, 75], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 76: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [4, 13, 22, 31, 40, 49, 58, 67, 76], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 77: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [5, 14, 23, 32, 41, 50, 59, 68, 77], [57, 58, 59, 66, 67, 68, 75, 76, 77]], 78: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [6, 15, 24, 33, 42, 51, 60, 69, 78], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 79: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [7, 16, 25, 34, 43, 52, 61, 70, 79], [60, 61, 62, 69, 70, 71, 78, 79, 80]], 80: [[72, 73, 74, 75, 76, 77, 78, 79, 80], [8, 17, 26, 35, 44, 53, 62, 71, 80], [60, 61, 62, 69, 70, 71, 78, 79, 80]]}
cliquemap2 = {0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 27, 36, 45, 54, 63, 72], 1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 28, 37, 46, 55, 64, 73], 2: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 18, 19, 20, 29, 38, 47, 56, 65, 74], 3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 30, 39, 48, 57, 66, 75], 4: [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 31, 40, 49, 58, 67, 76], 5: [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 13, 14, 21, 22, 23, 32, 41, 50, 59, 68, 77], 6: [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60, 69, 78], 7: [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 34, 43, 52, 61, 70, 79], 8: [0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 17, 24, 25, 26, 35, 44, 53, 62, 71, 80], 9: [0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 27, 36, 45, 54, 63, 72], 10: [0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 28, 37, 46, 55, 64, 73], 11: [0, 1, 2, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 29, 38, 47, 56, 65, 74], 12: [3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 30, 39, 48, 57, 66, 75], 13: [3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 31, 40, 49, 58, 67, 76], 14: [3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 32, 41, 50, 59, 68, 77], 15: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 33, 42, 51, 60, 69, 78], 16: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 34, 43, 52, 61, 70, 79], 17: [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 24, 25, 26, 35, 44, 53, 62, 71, 80], 18: [0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 36, 45, 54, 63, 72], 19: [0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 37, 46, 55, 64, 73], 20: [0, 1, 2, 9, 10, 11, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 38, 47, 56, 65, 74], 21: [3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 30, 39, 48, 57, 66, 75], 22: [3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 31, 40, 49, 58, 67, 76], 23: [3, 4, 5, 12, 13, 14, 18, 19, 20, 21, 22, 23, 24, 25, 26, 32, 41, 50, 59, 68, 77], 24: [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 33, 42, 51, 60, 69, 78], 25: [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 34, 43, 52, 61, 70, 79], 26: [6, 7, 8, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 35, 44, 53, 62, 71, 80], 27: [0, 9, 18, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 54, 63, 72], 28: [1, 10, 19, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 55, 64, 73], 29: [2, 11, 20, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 56, 65, 74], 30: [3, 12, 21, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 57, 66, 75], 31: [4, 13, 22, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 58, 67, 76], 32: [5, 14, 23, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39, 40, 41, 48, 49, 50, 59, 68, 77], 33: [6, 15, 24, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 60, 69, 78], 34: [7, 16, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 61, 70, 79], 35: [8, 17, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 51, 52, 53, 62, 71, 80], 36: [0, 9, 18, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 54, 63, 72], 37: [1, 10, 19, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 55, 64, 73], 38: [2, 11, 20, 27, 28, 29, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 56, 65, 74], 39: [3, 12, 21, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 57, 66, 75], 40: [4, 13, 22, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 58, 67, 76], 41: [5, 14, 23, 30, 31, 32, 36, 37, 38, 39, 40, 41, 42, 43, 44, 48, 49, 50, 59, 68, 77], 42: [6, 15, 24, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 60, 69, 78], 43: [7, 16, 25, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 61, 70, 79], 44: [8, 17, 26, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 51, 52, 53, 62, 71, 80], 45: [0, 9, 18, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 63, 72], 46: [1, 10, 19, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 64, 73], 47: [2, 11, 20, 27, 28, 29, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 56, 65, 74], 48: [3, 12, 21, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 57, 66, 75], 49: [4, 13, 22, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 58, 67, 76], 50: [5, 14, 23, 30, 31, 32, 39, 40, 41, 45, 46, 47, 48, 49, 50, 51, 52, 53, 59, 68, 77], 51: [6, 15, 24, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 60, 69, 78], 52: [7, 16, 25, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 61, 70, 79], 53: [8, 17, 26, 33, 34, 35, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 62, 71, 80], 54: [0, 9, 18, 27, 36, 45, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74], 55: [1, 10, 19, 28, 37, 46, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74], 56: [2, 11, 20, 29, 38, 47, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 72, 73, 74], 57: [3, 12, 21, 30, 39, 48, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77], 58: [4, 13, 22, 31, 40, 49, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77], 59: [5, 14, 23, 32, 41, 50, 54, 55, 56, 57, 58, 59, 60, 61, 62, 66, 67, 68, 75, 76, 77], 60: [6, 15, 24, 33, 42, 51, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80], 61: [7, 16, 25, 34, 43, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80], 62: [8, 17, 26, 35, 44, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 69, 70, 71, 78, 79, 80], 63: [0, 9, 18, 27, 36, 45, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], 64: [1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], 65: [2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74], 66: [3, 12, 21, 30, 39, 48, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77], 67: [4, 13, 22, 31, 40, 49, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77], 68: [5, 14, 23, 32, 41, 50, 57, 58, 59, 63, 64, 65, 66, 67, 68, 69, 70, 71, 75, 76, 77], 69: [6, 15, 24, 33, 42, 51, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80], 70: [7, 16, 25, 34, 43, 52, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80], 71: [8, 17, 26, 35, 44, 53, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 78, 79, 80], 72: [0, 9, 18, 27, 36, 45, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80], 73: [1, 10, 19, 28, 37, 46, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80], 74: [2, 11, 20, 29, 38, 47, 54, 55, 56, 63, 64, 65, 72, 73, 74, 75, 76, 77, 78, 79, 80], 75: [3, 12, 21, 30, 39, 48, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80], 76: [4, 13, 22, 31, 40, 49, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80], 77: [5, 14, 23, 32, 41, 50, 57, 58, 59, 66, 67, 68, 72, 73, 74, 75, 76, 77, 78, 79, 80], 78: [6, 15, 24, 33, 42, 51, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], 79: [7, 16, 25, 34, 43, 52, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80], 80: [8, 17, 26, 35, 44, 53, 60, 61, 62, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]}
def sudokuprint(board):
    return ''.join((str(board[n])+("," if n%9!=8 else "\n") for n in range(81)))
def possible(board,index):
    dumbhash = [True,True,True,True,True,True,True,True,True,True]
    for member in cliquemap2[index]:
        dumbhash[board[member]]=False
    if dumbhash[1]: yield 1
    if dumbhash[2]: yield 2
    if dumbhash[3]: yield 3
    if dumbhash[4]: yield 4
    if dumbhash[5]: yield 5
    if dumbhash[6]: yield 6
    if dumbhash[7]: yield 7
    if dumbhash[8]: yield 8
    if dumbhash[9]: yield 9
def elimcliques(board,index):
    chindices = []
    for clique in cliquemap[index]:
        dumbhash = [[],[],[],[],[],[],[],[],[],[]]
        for val in clique:
            if board[val]: continue
            for pos in possible(board,val):
                dumbhash[pos].append(val)
        if dumbhash[1] and len(dumbhash[1])==1:
            board[dumbhash[1][0]] = 1
            chindices.append(dumbhash[1][0])
        if dumbhash[2] and len(dumbhash[2])==1:
            board[dumbhash[2][0]] = 2
            chindices.append(dumbhash[2][0])
        if dumbhash[3] and len(dumbhash[3])==1:
            board[dumbhash[3][0]] = 3
            chindices.append(dumbhash[3][0])
        if dumbhash[4] and len(dumbhash[4])==1:
            board[dumbhash[4][0]] = 4
            chindices.append(dumbhash[4][0])
        if dumbhash[5] and len(dumbhash[5])==1:
            board[dumbhash[5][0]] = 5
            chindices.append(dumbhash[5][0])
        if dumbhash[6] and len(dumbhash[6])==1:
            board[dumbhash[6][0]] = 6
            chindices.append(dumbhash[6][0])
        if dumbhash[7] and len(dumbhash[7])==1:
            board[dumbhash[7][0]] = 7
            chindices.append(dumbhash[7][0])
        if dumbhash[8] and len(dumbhash[8])==1:
            board[dumbhash[8][0]] = 8
            chindices.append(dumbhash[8][0])
        if dumbhash[9] and len(dumbhash[9])==1:
            board[dumbhash[9][0]] = 9
            chindices.append(dumbhash[9][0])
    return len(chindices) + sum([elimcliques(board,i) for i in chindices])
 
def obviousget(board):
    changed = True
    guyschanged = []
    gappend = guyschanged.append
    while changed:
        changed = False
        if not board[0]:
            posarr = list(possible(board,0))
            if len(posarr)==1:
                board[0] = posarr[0]
                gappend(0)
                changed = True
        if not board[1]:
            posarr = list(possible(board,1))
            if len(posarr)==1:
                board[1] = posarr[0]
                gappend(1)
                changed = True
        if not board[2]:
            posarr = list(possible(board,2))
            if len(posarr)==1:
                board[2] = posarr[0]
                gappend(2)
                changed = True
        if not board[3]:
            posarr = list(possible(board,3))
            if len(posarr)==1:
                board[3] = posarr[0]
                gappend(3)
                changed = True
        if not board[4]:
            posarr = list(possible(board,4))
            if len(posarr)==1:
                board[4] = posarr[0]
                gappend(4)
                changed = True
        if not board[5]:
            posarr = list(possible(board,5))
            if len(posarr)==1:
                board[5] = posarr[0]
                gappend(5)
                changed = True
        if not board[6]:
            posarr = list(possible(board,6))
            if len(posarr)==1:
                board[6] = posarr[0]
                gappend(6)
                changed = True
        if not board[7]:
            posarr = list(possible(board,7))
            if len(posarr)==1:
                board[7] = posarr[0]
                gappend(7)
                changed = True
        if not board[8]:
            posarr = list(possible(board,8))
            if len(posarr)==1:
                board[8] = posarr[0]
                gappend(8)
                changed = True
        if not board[9]:
            posarr = list(possible(board,9))
            if len(posarr)==1:
                board[9] = posarr[0]
                gappend(9)
                changed = True
        if not board[10]:
            posarr = list(possible(board,10))
            if len(posarr)==1:
                board[10] = posarr[0]
                gappend(10)
                changed = True
        if not board[11]:
            posarr = list(possible(board,11))
            if len(posarr)==1:
                board[11] = posarr[0]
                gappend(11)
                changed = True
        if not board[12]:
            posarr = list(possible(board,12))
            if len(posarr)==1:
                board[12] = posarr[0]
                gappend(12)
                changed = True
        if not board[13]:
            posarr = list(possible(board,13))
            if len(posarr)==1:
                board[13] = posarr[0]
                gappend(13)
                changed = True
        if not board[14]:
            posarr = list(possible(board,14))
            if len(posarr)==1:
                board[14] = posarr[0]
                gappend(14)
                changed = True
        if not board[15]:
            posarr = list(possible(board,15))
            if len(posarr)==1:
                board[15] = posarr[0]
                gappend(15)
                changed = True
        if not board[16]:
            posarr = list(possible(board,16))
            if len(posarr)==1:
                board[16] = posarr[0]
                gappend(16)
                changed = True
        if not board[17]:
            posarr = list(possible(board,17))
            if len(posarr)==1:
                board[17] = posarr[0]
                gappend(17)
                changed = True
        if not board[18]:
            posarr = list(possible(board,18))
            if len(posarr)==1:
                board[18] = posarr[0]
                gappend(18)
                changed = True
        if not board[19]:
            posarr = list(possible(board,19))
            if len(posarr)==1:
                board[19] = posarr[0]
                gappend(19)
                changed = True
        if not board[20]:
            posarr = list(possible(board,20))
            if len(posarr)==1:
                board[20] = posarr[0]
                gappend(20)
                changed = True
        if not board[21]:
            posarr = list(possible(board,21))
            if len(posarr)==1:
                board[21] = posarr[0]
                gappend(21)
                changed = True
        if not board[22]:
            posarr = list(possible(board,22))
            if len(posarr)==1:
                board[22] = posarr[0]
                gappend(22)
                changed = True
        if not board[23]:
            posarr = list(possible(board,23))
            if len(posarr)==1:
                board[23] = posarr[0]
                gappend(23)
                changed = True
        if not board[24]:
            posarr = list(possible(board,24))
            if len(posarr)==1:
                board[24] = posarr[0]
                gappend(24)
                changed = True
        if not board[25]:
            posarr = list(possible(board,25))
            if len(posarr)==1:
                board[25] = posarr[0]
                gappend(25)
                changed = True
        if not board[26]:
            posarr = list(possible(board,26))
            if len(posarr)==1:
                board[26] = posarr[0]
                gappend(26)
                changed = True
        if not board[27]:
            posarr = list(possible(board,27))
            if len(posarr)==1:
                board[27] = posarr[0]
                gappend(27)
                changed = True
        if not board[28]:
            posarr = list(possible(board,28))
            if len(posarr)==1:
                board[28] = posarr[0]
                gappend(28)
                changed = True
        if not board[29]:
            posarr = list(possible(board,29))
            if len(posarr)==1:
                board[29] = posarr[0]
                gappend(29)
                changed = True
        if not board[30]:
            posarr = list(possible(board,30))
            if len(posarr)==1:
                board[30] = posarr[0]
                gappend(30)
                changed = True
        if not board[31]:
            posarr = list(possible(board,31))
            if len(posarr)==1:
                board[31] = posarr[0]
                gappend(31)
                changed = True
        if not board[32]:
            posarr = list(possible(board,32))
            if len(posarr)==1:
                board[32] = posarr[0]
                gappend(32)
                changed = True
        if not board[33]:
            posarr = list(possible(board,33))
            if len(posarr)==1:
                board[33] = posarr[0]
                gappend(33)
                changed = True
        if not board[34]:
            posarr = list(possible(board,34))
            if len(posarr)==1:
                board[34] = posarr[0]
                gappend(34)
                changed = True
        if not board[35]:
            posarr = list(possible(board,35))
            if len(posarr)==1:
                board[35] = posarr[0]
                gappend(35)
                changed = True
        if not board[36]:
            posarr = list(possible(board,36))
            if len(posarr)==1:
                board[36] = posarr[0]
                gappend(36)
                changed = True
        if not board[37]:
            posarr = list(possible(board,37))
            if len(posarr)==1:
                board[37] = posarr[0]
                gappend(37)
                changed = True
        if not board[38]:
            posarr = list(possible(board,38))
            if len(posarr)==1:
                board[38] = posarr[0]
                gappend(38)
                changed = True
        if not board[39]:
            posarr = list(possible(board,39))
            if len(posarr)==1:
                board[39] = posarr[0]
                gappend(39)
                changed = True
        if not board[40]:
            posarr = list(possible(board,40))
            if len(posarr)==1:
                board[40] = posarr[0]
                gappend(40)
                changed = True
        if not board[41]:
            posarr = list(possible(board,41))
            if len(posarr)==1:
                board[41] = posarr[0]
                gappend(41)
                changed = True
        if not board[42]:
            posarr = list(possible(board,42))
            if len(posarr)==1:
                board[42] = posarr[0]
                gappend(42)
                changed = True
        if not board[43]:
            posarr = list(possible(board,43))
            if len(posarr)==1:
                board[43] = posarr[0]
                gappend(43)
                changed = True
        if not board[44]:
            posarr = list(possible(board,44))
            if len(posarr)==1:
                board[44] = posarr[0]
                gappend(44)
                changed = True
        if not board[45]:
            posarr = list(possible(board,45))
            if len(posarr)==1:
                board[45] = posarr[0]
                gappend(45)
                changed = True
        if not board[46]:
            posarr = list(possible(board,46))
            if len(posarr)==1:
                board[46] = posarr[0]
                gappend(46)
                changed = True
        if not board[47]:
            posarr = list(possible(board,47))
            if len(posarr)==1:
                board[47] = posarr[0]
                gappend(47)
                changed = True
        if not board[48]:
            posarr = list(possible(board,48))
            if len(posarr)==1:
                board[48] = posarr[0]
                gappend(48)
                changed = True
        if not board[49]:
            posarr = list(possible(board,49))
            if len(posarr)==1:
                board[49] = posarr[0]
                gappend(49)
                changed = True
        if not board[50]:
            posarr = list(possible(board,50))
            if len(posarr)==1:
                board[50] = posarr[0]
                gappend(50)
                changed = True
        if not board[51]:
            posarr = list(possible(board,51))
            if len(posarr)==1:
                board[51] = posarr[0]
                gappend(51)
                changed = True
        if not board[52]:
            posarr = list(possible(board,52))
            if len(posarr)==1:
                board[52] = posarr[0]
                gappend(52)
                changed = True
        if not board[53]:
            posarr = list(possible(board,53))
            if len(posarr)==1:
                board[53] = posarr[0]
                gappend(53)
                changed = True
        if not board[54]:
            posarr = list(possible(board,54))
            if len(posarr)==1:
                board[54] = posarr[0]
                gappend(54)
                changed = True
        if not board[55]:
            posarr = list(possible(board,55))
            if len(posarr)==1:
                board[55] = posarr[0]
                gappend(55)
                changed = True
        if not board[56]:
            posarr = list(possible(board,56))
            if len(posarr)==1:
                board[56] = posarr[0]
                gappend(56)
                changed = True
        if not board[57]:
            posarr = list(possible(board,57))
            if len(posarr)==1:
                board[57] = posarr[0]
                gappend(57)
                changed = True
        if not board[58]:
            posarr = list(possible(board,58))
            if len(posarr)==1:
                board[58] = posarr[0]
                gappend(58)
                changed = True
        if not board[59]:
            posarr = list(possible(board,59))
            if len(posarr)==1:
                board[59] = posarr[0]
                gappend(59)
                changed = True
        if not board[60]:
            posarr = list(possible(board,60))
            if len(posarr)==1:
                board[60] = posarr[0]
                gappend(60)
                changed = True
        if not board[61]:
            posarr = list(possible(board,61))
            if len(posarr)==1:
                board[61] = posarr[0]
                gappend(61)
                changed = True
        if not board[62]:
            posarr = list(possible(board,62))
            if len(posarr)==1:
                board[62] = posarr[0]
                gappend(62)
                changed = True
        if not board[63]:
            posarr = list(possible(board,63))
            if len(posarr)==1:
                board[63] = posarr[0]
                gappend(63)
                changed = True
        if not board[64]:
            posarr = list(possible(board,64))
            if len(posarr)==1:
                board[64] = posarr[0]
                gappend(64)
                changed = True
        if not board[65]:
            posarr = list(possible(board,65))
            if len(posarr)==1:
                board[65] = posarr[0]
                gappend(65)
                changed = True
        if not board[66]:
            posarr = list(possible(board,66))
            if len(posarr)==1:
                board[66] = posarr[0]
                gappend(66)
                changed = True
        if not board[67]:
            posarr = list(possible(board,67))
            if len(posarr)==1:
                board[67] = posarr[0]
                gappend(67)
                changed = True
        if not board[68]:
            posarr = list(possible(board,68))
            if len(posarr)==1:
                board[68] = posarr[0]
                gappend(68)
                changed = True
        if not board[69]:
            posarr = list(possible(board,69))
            if len(posarr)==1:
                board[69] = posarr[0]
                gappend(69)
                changed = True
        if not board[70]:
            posarr = list(possible(board,70))
            if len(posarr)==1:
                board[70] = posarr[0]
                gappend(70)
                changed = True
        if not board[71]:
            posarr = list(possible(board,71))
            if len(posarr)==1:
                board[71] = posarr[0]
                gappend(71)
                changed = True
        if not board[72]:
            posarr = list(possible(board,72))
            if len(posarr)==1:
                board[72] = posarr[0]
                gappend(72)
                changed = True
        if not board[73]:
            posarr = list(possible(board,73))
            if len(posarr)==1:
                board[73] = posarr[0]
                gappend(73)
                changed = True
        if not board[74]:
            posarr = list(possible(board,74))
            if len(posarr)==1:
                board[74] = posarr[0]
                gappend(74)
                changed = True
        if not board[75]:
            posarr = list(possible(board,75))
            if len(posarr)==1:
                board[75] = posarr[0]
                gappend(75)
                changed = True
        if not board[76]:
            posarr = list(possible(board,76))
            if len(posarr)==1:
                board[76] = posarr[0]
                gappend(76)
                changed = True
        if not board[77]:
            posarr = list(possible(board,77))
            if len(posarr)==1:
                board[77] = posarr[0]
                gappend(77)
                changed = True
        if not board[78]:
            posarr = list(possible(board,78))
            if len(posarr)==1:
                board[78] = posarr[0]
                gappend(78)
                changed = True
        if not board[79]:
            posarr = list(possible(board,79))
            if len(posarr)==1:
                board[79] = posarr[0]
                gappend(79)
                changed = True
        if not board[80]:
            posarr = list(possible(board,80))
            if len(posarr)==1:
                board[80] = posarr[0]
                gappend(80)
                changed = True
    return len(guyschanged) + sum((elimcliques(board,i) for i in guyschanged))
def obviousishget(board):
    start = 0
    try:
        while board[start]:
            start+=1
    except:
        return 81,None
    for i in range(start,81):
        if not board[i]:
            posarrl = list(possible(board,i))
            posarr = len(posarrl)
            if posarr<4: return i,posarrl
    return start,possible(board,start)

def solveboard(board,index):
    #global backtracks
    board = board[:]
    elimcliques(board,index)
    while obviousget(board): pass
    elimcliques(board,0)
    elimcliques(board,12)
    elimcliques(board,24)
    elimcliques(board,28)
    elimcliques(board,40)
    elimcliques(board,52)
    elimcliques(board,56)
    elimcliques(board,68)
    elimcliques(board,80)
    index,poss = obviousishget(board)
    if index==81:
        outputfile.write(sudokuprint(board))
        #print(backtracks)
        sys.exit(0)
    #genlen = 0
    poss = list(poss)
    for n in poss:
        board[index] = n
        solveboard(board,index)
        #genlen+=1
    #if genlen!=1:
        #backtracks+=1
    return
with open(sys.argv[1],'r') as inputfile, open(sys.argv[2],'w') as outputfile:
    while inputfile.readline().strip()!=sys.argv[3]: pass
    board = [int(x) for x in ','.join((inputfile.readline().strip() for i in range(9))).replace("_",'0').split(',')]
    obviousget(board)
    elimcliques(board,0)
    elimcliques(board,12)
    elimcliques(board,24)
    elimcliques(board,28)
    elimcliques(board,40)
    elimcliques(board,52)
    elimcliques(board,56)
    elimcliques(board,68)
    elimcliques(board,80)
    index = 0
    try:
        while(board[index]):
            index+=1
    except:
        outputfile.write(sudokuprint(board))
        sys.exit(0)
    solveboard(board,index)
