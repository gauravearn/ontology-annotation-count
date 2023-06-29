# changed the names of the iterable as the names were those which i used in testing iterables :-)
import arguably
import pandas as pd
@arguably.command
def prepareGeneEnrichment(file = False, count= False, annotation = False):
    """
    _summary_
    A parser to prepare the files for the functional
    enrichment of the gene categories across the 
    functionally annotated microbiome
    Arguments:
        file -- _description_
        a text file containing your gene ontologies
    """
    if file:
        go_content = []
        go_summarize = []
        with open(file, 'r') as file:
            for line in file.readlines():
                go_content.append(line.strip())
            for i in range(len(file_go)):
                go_summarize.append(go_content[i].replace(";", ""))
    if file and count:
           go_content = []
           go_summarize = []
           go_count = []
           with open(file, 'r') as file:
            for line in file.readlines():
                go_content.append(line.strip())
            for i in range(len(go_content)):
                go_summarize.append(go_content[i].replace(";", "")) 
                go_count.append([{i:gene_summarize.count(i)} for i in set(go_summarize)])
                return go_content, go_summarize, go_count
    if annotation:
        while True:
            take_annotation = input("Please enter the path for the \
                               annotation file")
            take_annotation_col = input("Please enter the annotation columns")
            annotations = pd.read_csv("take_annotation", sep = ",")
            annotations_col = annotations["take_annotation_col"].dropna().tolist()
            final_annotations = [row for col in ([i.split(";") for i in go]) for row in col]
            final_annotations_count = [{i:final_annotations.count(i)} for i in set(final_annotations)]
            annotations_name = [i for i in set(final_annotations)]
            annotations_count = [final_annotations.count(i) for i in set(final_annotations_count)]
            annotations_dataframe = pd.DataFrame([(i,j)for i,j in zip(annotations_count, annotations_name)])
        return final_annotations, final_annotations_count, annotations_name, annotations_dataframe   
    if __name__ == "__main__":
    arguably.run()         
