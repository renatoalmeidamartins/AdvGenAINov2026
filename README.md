# AdvGenAINov2026

## Labs, courseware, survey...
- [Labs and courseware access](https://us-east-1.student.classrooms.aws.training/class/ilt%23a19i4KWVipSdHCdpg5yXs3)

## Content links
### Day 1
- Well-architected framework
    - [AWS](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html), notice how AWS's pillars are about the same as the ones on [GCP's](https://docs.cloud.google.com/architecture/framework) and [Azure's](https://learn.microsoft.com/en-us/azure/well-architected/pillars) well architect framework
    - [Well-architected agent](https://docs.aws.amazon.com/wellarchitected/latest/userguide/agent-getting-started.html)
    - [Lens Catalog for AWS Well-Architected Tool](https://docs.aws.amazon.com/wellarchitected/latest/userguide/lens-catalog.html)
    - [Machine Learning Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/machine-learning-lens.html)
    - [Generative AI Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lens.html)
- [Evaluate model performance using another LLM as a judge](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Prompt templates for the Agentcore evaluators](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/prompt-templates-builtin.html)
- Common model provider APIs
    - [Anthropic's Messages](https://platform.claude.com/docs/en/api/messages)
    - [OpenAI's responses](https://developers.openai.com/api/reference/resources/responses/methods/create)
    - [Try the new console experience in Amazon Bedrock, optimized for Anthropic- and OpenAI-compatible APIs](https://aws.amazon.com/blogs/aws/try-the-new-console-experience-in-amazon-bedrock-optimized-for-anthropic-and-openai-compatible-apis/)
- [Deploying and Managing Application Configurations using AWS AppConfig](https://aws.amazon.com/blogs/devops/deploying-and-managing-application-configurations-using-aws-appconfig/)
- [One way of having adapters - Langchain Messages](https://docs.langchain.com/oss/python/langchain/models#google-gemini)
- Intelligent prompt routing 
    - [Documentation of current support on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
    - [IPR: Intelligent Prompt Routing with User-Controlled Quality-Cost Trade-offs](https://arxiv.org/html/2509.06274v3), research article that led to the implementation of Bedrock Intelligent prompt routing
- [Inference profiles in Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html) - used for cross-region inference (and application-level inference profiles)
- [Disaster recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [Prompt caching in Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [LangChain Memory](https://docs.langchain.com/oss/python/concepts/memory)
- [Optimize model inference for latency](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- RAG - Retrieval Augmented Generation
    - [What is RAG?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
    - [What are Embeddings in Machine Learning?](https://aws.amazon.com/what-is/embeddings-in-machine-learning/)
    - [What is a Vector Database?](https://aws.amazon.com/what-is/vector-databases/)
    - [Introducing Amazon S3 Vectors: First cloud storage with native vector support at scale (preview)](https://aws.amazon.com/blogs/aws/introducing-amazon-s3-vectors-first-cloud-storage-with-native-vector-support-at-scale/), announced in July 2025. Became GA in December 2025, "[Amazon S3 Vectors now generally available with increased scale and performance](https://aws.amazon.com/blogs/aws/amazon-s3-vectors-now-generally-available-with-increased-scale-and-performance/)"
    - [Vector projection visualizer](https://projector.tensorflow.org/)
    - [Amazon Bedrock Knowledge Bases now supports Amazon OpenSearch Service Managed Cluster as vector store](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-amazon-opensearch-service-managed-cluster-as-vector-store/)
    - [Choose the k-NN algorithm for your billion-scale use case with OpenSearch](https://aws.amazon.com/blogs/big-data/choose-the-k-nn-algorithm-for-your-billion-scale-use-case-with-opensearch/)
    - [Build semantic search with native vector support in Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-semantic-search-with-native-vector-support-in-amazon-dynamodb/)
    - [Amazon DynamoDB now supports real-time vector search at any scale](https://aws.amazon.com/blogs/aws/amazon-dynamodb-now-supports-real-time-vector-search-at-any-scale/)
    - [Amazon Bedrock Knowledge Bases now supports hybrid search](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-hybrid-search/)
    - [How content chunking works for knowledge bases](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html)
    - [Super charge your LLMs with RAG at scale using AWS Glue for Apache Spark](https://aws.amazon.com/blogs/machine-learning/super-charge-your-llms-with-rag-at-scale-using-aws-glue-for-apache-spark/)
    - [List of available metrics in RAGAS](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/)
    - [Evaluator prompts used in a RAG evaluation job](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-eval-prompt.html)
    - [New RAG evaluation and LLM-as-a-judge capabilities in Amazon Bedrock ](https://aws.amazon.com/blogs/aws/new-rag-evaluation-and-llm-as-a-judge-capabilities-in-amazon-bedrock/)
    - [Introducing Amazon Bedrock Managed Knowledge Base for faster, more accurate enterprise AI applications](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-managed-knowledge-base-for-faster-more-accurate-enterprise-ai-applications/)
### Day 2