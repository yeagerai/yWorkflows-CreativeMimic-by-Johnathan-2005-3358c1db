
# CreativeMimic

The CreativeMimic component is designed to generate an article on a desired topic by mimicking the writing style of the provided writing samples. The component analyses the input writing samples, extracts specific features like sentence structures, vocabulary, and tone, and then combines these features with the desired topic to generate a creative and coherent article. This component aims to create an article that matches the quality and style of the input writing samples while covering the desired topic effectively.

## Initial generation prompt
description: 'IOs - ''Inputs: WritingSamplesUpload, DesiredTopic. Outputs: GeneratedArticle.''

  '
name: CreativeMimic


## Transformer breakdown
- Load writing samples from WritingSamplesUpload input.
- Choose style_features_extraction_method.
- Extract style features from the writing samples using the chosen method.
- Choose content_generation_algorithm.
- Generate article content by combining the extracted style features and the DesiredTopic using the chosen algorithm.
- Return the GeneratedArticle as output.

## Parameters
[{'name': 'style_features_extraction_method', 'default_value': 'default', 'description': 'The method to be used for extracting style features from the writing samples. Default method will be used if not specified.', 'type': 'string'}, {'name': 'content_generation_algorithm', 'default_value': 'transformers', 'description': 'The algorithm to be used to generate the article content based on extracted style features and desired topic. Transformers-based algorithm will be used if not specified.', 'type': 'string'}]

        