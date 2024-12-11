import numpy as np
import pandas as pd

def list_list(l: list[list[float | int | str]], accuracy: int = 4) -> None:
    for ll in l:
        print("-"*10)
        for x in ll:
            print(f"{x:.{accuracy}f}")

def list1D(l: list[list[float | int | str]], accuracy: int = 4) -> None:
        for x in l:
            print(f"{x:.{accuracy}f}")

def mat(mat: np.ndarray, accuracy: int = 4) -> None:
    for row in mat:
        print(f"|", end="")
        for col in row:
            print(f" {col:.{accuracy}f} ", end="")
        print("|")
     
def mat_nxu(mat: np.ndarray, row_names: list[str] = None, col_names: list[str] = None, accuracy: int = 4) -> None:
    if not row_names:
        row_names = [f"l{i + 1}" for i in range(mat.shape[0])]
    if not col_names:
        col_names = [f"u{i + 1}" for i in range(mat.shape[1])]

    df = pd.DataFrame(mat, index=row_names, columns=col_names)
    
    df = df.round(accuracy)

    print(df.head(mat.shape[0]))
     
def mat_nxn(mat: np.ndarray, names: list[str] = None, accuracy: int = 4, unknonws: bool = False) -> None:
    if not names:
        if not unknonws:
            names = [f"l{i + 1}" for i in range(mat.shape[0])]
        else:
            names = [f"u{i + 1}" for i in range(mat.shape[0])]

    df = pd.DataFrame(mat, index=names, columns=names)
    
    df = df.round(accuracy)

    print(df.head(mat.shape[0]))
    
def vect(l: list[list[float | int | str]], accuracy: int = 4, row_names: list[str] = None, unknowns=False, title: str = "") -> None:
    # Dynamische Formatierung basierend auf accuracy
    pd.set_option('display.float_format', f'{{:.{accuracy}f}}'.format)
    
    if not row_names:
        if not unknowns:
            row_names = [f"l{i + 1}" for i in range(len(l))]
        else:
            row_names = [f"u{i + 1}" for i in range(len(l))]
    
    df = pd.DataFrame({title: l}, index=row_names)
    
    df = df.applymap(lambda x: round(x, accuracy) if isinstance(x, (int, float)) else x)
    
    # Ausgabe des DataFrames
    print(df)
