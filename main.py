from binaryheap import BinaryHeap

def executar_teste(nome: str, heap: BinaryHeap, dados: list, alteracoes: list, removals: int):
    print(f"====================== {nome} ======================")
    
    for valor in dados:
        heap.insert(valor)
        heap.print_tree()
    
    for idx, novo_valor in alteracoes:
        heap.change_priority(idx, novo_valor)
        heap.print_tree()
    
    for _ in range(removals):
        print(f"Removendo: {heap.remove()}")
        heap.print_tree()
    
    heap.ordenar()
    heap.print_tree()
    print("High priority:", heap.get_high_priority())
    print("=====================================================")

if __name__ == '__main__':
    heap = BinaryHeap()
    
    executar_teste("Conjunto 1", heap, dados=[10, 5, 20, 1, 15, 30, 25], 
                   alteracoes=[(3, 50), (1, 8)], removals=3)
    
    executar_teste("Conjunto 2", heap, dados=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                   alteracoes=[(4, 15), (8, 3)], removals=5)
    
    executar_teste("Conjunto 3", heap, dados=[50, 40, 30, 20, 10, 5, 3], 
                   alteracoes=[(2, 60)], removals=3)
    
    executar_teste("Conjunto 4", heap, dados=[13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18], 
                   alteracoes=[(7, 35), (10, 12)], removals=4)
