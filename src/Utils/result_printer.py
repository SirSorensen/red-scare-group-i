

import os
from Gallery_of_Graphs.graph import Graph
from Utils.graph_factory import construct_graph
from os import listdir
from os.path import isfile, join


def solve_all(g : Graph) -> dict:
    return {
        "none" : try_solve(g.solve_none),
        "some" : try_solve(g.solve_some),
        "many" : try_solve(g.solve_many),
        "few" : try_solve(g.solve_few),
        "alternate" : try_solve(g.solve_alternate)
    }

def try_solve(f) -> str:
    try:
        result = f()
    except:
        result = "?"
    return result


def print_solution(file_name : str):
    g : Graph = construct_graph(file_name)
    solutions = solve_all(g)
        
    result = ""
    result += f"None: {solutions["none"]}\n"
    result += f"Some: {solutions["some"]}\n"
    result += f"Many: {solutions["many"]}\n"
    result += f"Few: {solutions["few"]}\n"
    result += f"Alternate: {solutions["alternate"]}\n"
    print(result)
    return result

def print_all_solutions(print_to_file = False):
    files = get_all_files()
    files.sort()

    results = []
    for file in files:
        print(file)
        results.append(file + '\n' + print_solution(file))
    
    print_result = '\n'.join(results)

    if print_to_file:
        output_to_file(print_result)

def put_into_latex_table(results : list[dict]) -> str:
    result =  r"\begin{longtable}{lrrrrrrr}" + "\n"
    result += r"  \toprule" + "\n"
    result += r"  Instance name & $|V(G)|$ & $|E(G)|$ & Alternate & Few & Many & None & Some \\" + "\n"
    result += r"  \midrule" + "\n"
    result += r"  \endhead" + "\n"
    result += r"  \bottomrule" + "\n"
    result += r"  \endfoot" + "\n"
    result += r"  \bottomrule" + "\n"
    result += r"  \caption{Table containing the results for all graphs of at least 500 vertices}" + "\n"
    result += r"  \endlastfoot" + "\n"
    for cur_result in results:
        result += r"  "
        result += f"{cur_result["name"]} & "
        result += f"{cur_result["n"]} & "
        result += f"{cur_result["m"]} & "
        result += f"{cur_result["alternate"]} & "
        result += f"{cur_result["few"]} & "
        result += f"{cur_result["many"]} & "
        result += f"{cur_result["none"]} & "
        result += f"{cur_result["some"]} \\\\\n"
    result += r"\end{longtable}" + "\n"
    return result

def _get_results(files : list):
    results = []
    for file_name in files:
        g = construct_graph(file_name)
        if g.node_amount >= 500:
            cur_result = solve_all(g)
            cur_result["n"] = g.node_amount
            cur_result["m"] = g.edge_amount
            cur_result["name"] = file_name
            results.append(cur_result)
    return results

def print_latex_table(print_to_file = False):
    print("Print latex table...\n")
    files = get_all_files()
    files.sort()
    results = _get_results(files)
    print_result = put_into_latex_table(results)
    print(print_result)
    if print_to_file:
        output_to_file(print_result)
    return print_result
    



def get_all_files():
    abs_path = _get_data_path()
    return [f for f in listdir(abs_path) if isfile(join(abs_path, f))]

def _get_data_path():
    abs_path = os.path.abspath(os.getcwd())
    dir_path : str = "/data"
    if os.path.exists(abs_path + dir_path):
        return abs_path + dir_path
    
    dir_path : str = "/../data"
    if os.path.exists(abs_path + dir_path):
        return abs_path + dir_path
    
    raise FileNotFoundError()

def output_to_file(output : str, file_location : str = "output.txt"):
    f = open(file_location, "w")
    f.write(output)
    f.close()