from lxml import etree
from xml.dom.minidom import parse
import xml.dom.minidom
import os

class ParseTRX:
    def Parse(self, filePath):
        with open(filePath, 'r', encoding='utf_8') as f:
            content = f.read()
        # 将文件内容解析为Element对象
        root = etree.fromstring(content)
        print(root)

        # 获取测试结果节点
        test_results_node = root.find('TestRun')
        print(test_results_node)
        # 遍历测试结果节点获取每个测试用例的执行结果
        for test_result_node in test_results_node.iter('UnitTestResult'):
            test_name = test_result_node.get('testName')
            outcome = test_result_node.get('outcome')
            duration = test_result_node.get('duration')
            print('eee')
            print(f'Test case:{test_name},outcome:{outcome},duration:{duration}')

    def ParseByDoc(self, filePath):
        # 使用minidom解析器打开 XML 文档
        DOMTree = xml.dom.minidom.parse(filePath)
        collection = DOMTree.documentElement
        if collection.hasAttribute("name"):
            print("Root element : %s" % collection.getAttribute("name"))

        # 获取测试结果
        Results = collection.getElementsByTagName("Results")
        UnitTestResults = collection.getElementsByTagName("UnitTestResult")
        TestListOutCome ={}
        TestOutCome ={}

        for UnitTestResult in UnitTestResults:
            testOutCome = ""
            testName = ""
            testListId = ""
            if (UnitTestResult.hasAttribute("testName")):
                testName = UnitTestResult.getAttribute("testName")
                print("testName:" + testName)
            if (UnitTestResult.hasAttribute("testListId")):
                testListId = UnitTestResult.getAttribute("testListId")
                print("testListId:" +testListId)
            if (UnitTestResult.hasAttribute("outcome")):
                testOutCome = UnitTestResult.getAttribute("outcome")
                print("outcome:"+testOutCome)
            if (UnitTestResult.hasAttribute("executionId")):
                executionId = UnitTestResult.getAttribute("executionId")
                print("executionId:" +executionId)
            TestOutCome[testName] = testOutCome
            TestListOutCome[testListId] = TestOutCome
            print("------------------TestOutCome-------------")
            print(TestListOutCome)


        # 遍历每一个单元测试定义
        TestDefinitions = collection.getElementsByTagName("TestDefinitions")
        UnitTests = collection.getElementsByTagName("UnitTest")
        print("--------遍历每一个单元测试结果-------------")
        #遍历每一个单元测试结果
        TestDll={}
        for UnitTest in UnitTests:
            Execution = UnitTest.getElementsByTagName("Execution")
            ExecutionId = Execution[0].getAttribute("id")
            Storage = ''
            TestName = ""
            print("executionId:" + ExecutionId)
            if (UnitTest.hasAttribute("name")):
                TestName = UnitTest.getAttribute("name")
                print("name:" + TestName)
            if (UnitTest.hasAttribute("storage")):
                Storage = UnitTest.getAttribute("storage")
                print("storage:" + Storage)
                #TestDll[ExecutionId] = UnitTest.getAttribute("storage")
                TestDll.setdefault(Storage,[]).append(TestName)
        print(TestDll)
        for storage,TestNames in TestDll.items():
            print(storage)
            for TestName in TestNames:
                if(TestName in TestOutCome):
                    if(TestOutCome[TestName] == "Failed"):
                        print(TestName+"\t"+TestOutCome[TestName])

            # break

        TestLists = collection.getElementsByTagName("TestLists")

        # 获取Summary
        ResultSummary = collection.getElementsByTagName("ResultSummary")
        UTResult = ResultSummary[0].getAttribute("outcome")
        # 获取Summary Counters
        Summary_Counters = collection.getElementsByTagName("Counters")
        totalCounters  = Summary_Counters[0].getAttribute("total")
        executedCounters  = Summary_Counters[0].getAttribute("executed")
        SkippedCounters   = Summary_Counters[0].getAttribute("notExecuted")

        passedCounters  = Summary_Counters[0].getAttribute("passed")
        failedCounters  = Summary_Counters[0].getAttribute("failed")
        passpercentage = int(passedCounters)/int(totalCounters)
        f1 = lambda x:'%.2f%%' % (x*100)

        print("-------------------------------Summary----------------------------------")
        print("UTResult:"+UTResult)
        print("\ttotalCounters:"+totalCounters)
        print("\texecutedCounters:"+executedCounters)
        print("\tSkippedCounters:"+SkippedCounters)

        print("\tpassedCounters:"+passedCounters)

        print("\tfailedCounters:"+failedCounters)
        print("\tpasspercentage:{passpercentage}".format(passpercentage="%.2f%%" % (passpercentage * 100)))

        # 获取Summary CollectorDataEntries
        Collectors = collection.getElementsByTagName("Collector")
        for collector in Collectors:
            if(collector.hasAttribute("collectorDisplayName")):
                collectorDisplayName = collector.getAttribute("collectorDisplayName")
                if(collectorDisplayName == "Code Coverage"):
                    collector.getAttribute("collectorDisplayName")
                    nodes = collector.childNodes
                    print(nodes[1])
                    uriAttachments = nodes[1].getElementsByTagName("UriAttachment")
                    uriAttachment = uriAttachments[0].childNodes
                    codeCoverageHref = uriAttachment[1].getAttribute("href")
                    print("codeCoverage Path:"+codeCoverageHref)
                    Deployment = collection.getElementsByTagName("Deployment")
                    #通过组合runDeploymentRoot的值和href的值获取codeCoverage的相对路径
                    if(Deployment[0].hasAttribute("runDeploymentRoot")):
                        runDeploymentRoot = Deployment[0].getAttribute("runDeploymentRoot")
                        codeCoveragePath = os.path.join(os.getcwd(),'TestResults',runDeploymentRoot,'In/',codeCoverageHref)
                        print(codeCoveragePath)

                    break

if __name__ == '__main__':
    # ParseTRX().Parse("F:\\MYL\\Project\\PythonFiles\\Feishu\\UT.trx")
    ParseTRX().ParseByDoc("F:\\MYL\\Project\\PythonProjects\\CS_UT.trx")
