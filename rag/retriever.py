from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma

# LOAD EMBEDDING MODEL

embedding_model = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"

)

# LOAD VECTOR DB

vector_db = Chroma(

    persist_directory="vector_store",

    embedding_function=embedding_model

)

# RETRIEVER

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)