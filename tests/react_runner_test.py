import unittest

from inverted_react.react_runner import parseOutput

class ReactRunnerTest(unittest.TestCase):
    def testParsedOutput(self):
        self.assertEqual(parseOutput("""
Line that should not be in parsed output
Thought: some
thought
Action: some action
and more

Observation: some observation
Empty:
"""), {
    "Thought": "some\nthought",
    "Action": "some action\nand more",
    "Observation": "some observation",
    "Empty": "",
})

    def testParsedOutputUsesLastValue(self):
        self.assertEqual(parseOutput("""
Some Key: some value 1
Some Key: some value 2
"""), {
    "Some Key": "some value 2",
})
