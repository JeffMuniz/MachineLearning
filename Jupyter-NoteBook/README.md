Add-AzureAccount
Connect-AZAccount

New-AzResourceGroupDeployment `
  -Name AzResourceGroupDeployment `
  -ResourceGroupName MachiRG `
  -TemplateFile c:\MyTemplates\azuredeploy.json


  
A implantação pode levar alguns minutos para ser concluída.
Implantar modelo remoto
Em vez de armazenar modelos de ARM em seu computador local, você pode preferir armazená-los em um local externo. É possível armazenar modelos em um repositório de controle de código-fonte (como o GitHub). Ou ainda armazená-los em uma conta de armazenamento do Azure para acesso compartilhado na sua organização.
Se você estiver implantando em um grupo de recursos que não existe, crie o grupo de recursos. O nome do grupo de recursos pode incluir somente caracteres alfanuméricos, pontos, sublinhados, hifens e parênteses. Pode ter até 90 caracteres. O nome não pode terminar com um ponto.
Azure PowerShell


New-AzSubscriptionDeployment -Location brasilsouth -TemplateFile 

New-AzManagementGroupDeployment -Location <location> -TemplateFile <path-to-template>
Para saber mais sobre implantações de nível de grupo de gerenciamento, confira Criar recursos no nível de grupo de gerenciamento.
Para implantar em um locatário, use New-AzTenantDeployment.
Azure PowerShell

Copiar
New-AzTenantDeployment -Location <location> -TemplateFile <path-to-template>
Para saber mais sobre implantações de nível de locatário, confira Criar recursos no nível de locatário.
Para cada escopo, o usuário que está implantando o modelo deve ter as permissões necessárias para criar recursos.
Implantar o modelo local
Você pode implantar um modelo de seu computador local ou um que esteja armazenado externamente. Esta seção descreve a implantação de um modelo local.
Se você estiver implantando em um grupo de recursos que não existe, crie o grupo de recursos. O nome do grupo de recursos pode incluir somente caracteres alfanuméricos, pontos, sublinhados, hifens e parênteses. Pode ter até 90 caracteres. O nome não pode terminar com um ponto.
Azure PowerShell

Copiar
New-AzResourceGroup -Name ExampleGroup -Location "Central US"
Para implantar um modelo local, use o -TemplateFile parâmetro no comando de implantação. O exemplo a seguir também mostra como definir um valor de parâmetro proveniente do modelo.
Azure PowerShell


Copiar
New-AzResourceGroup -Name ExampleGroup -Location "Central US"
Para implantar um modelo externo, use o parâmetro -TemplateUri.
Azure PowerShell

Copiar
New-AzResourceGroupDeployment `
  -Name ExampleDeployment `
  -ResourceGroupName ExampleGroup `
  -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-storage-account-create/azuredeploy.json
O exemplo anterior requer um URI acessível publicamente para o modelo, que funciona para a maioria dos cenários porque seu modelo não deve incluir dados confidenciais. Se você precisar especificar dados confidenciais (como uma senha de administrador), passe esse valor como um parâmetro seguro. No entanto, se você quiser gerenciar o acesso ao modelo, considere o uso de especificações de modelo.
Nome da implantação
Ao implantar um modelo do ARM, você pode dar um nome à implantação. Esse nome pode ajudá-lo a recuperar a implantação do histórico de implantação. Se você não fornecer um nome para a implantação, o nome do arquivo de modelo será usado. Por exemplo, se você implantar um modelo chamado azuredeploy.json e não especificar um nome de implantação, a implantação será nomeada azuredeploy .
Toda vez que você executa uma implantação, uma entrada é adicionada ao histórico de implantação do grupo de recursos com o nome da implantação. Se você executar outra implantação e fornecer o mesmo nome, a entrada anterior será substituída pela implantação atual. Se você quiser manter entradas exclusivas no histórico de implantação, dê a cada implantação um nome exclusivo.
Para criar um nome exclusivo, você pode atribuir um número aleatório.
Azure PowerShell

Copiar

Experimente
$suffix = Get-Random -Maximum 1000
$deploymentName = "ExampleDeployment" + $suffix
Ou adicione um valor de data.
Azure PowerShell

Copiar

Experimente
$today=Get-Date -Format "MM-dd-yyyy"
$deploymentName="ExampleDeployment"+"$today"
Se você executar implantações simultâneas no mesmo grupo de recursos com o mesmo nome de implantação, somente a última implantação será concluída. Todas as implantações com o mesmo nome que não foram concluídas são substituídas pela última implantação. Por exemplo, se você executar uma implantação chamada newStorage que implanta uma conta de armazenamento denominada storage1 e, ao mesmo tempo, executar outra implantação chamada newStorage que implanta uma conta de armazenamento denominada storage2 , você implanta apenas uma conta de armazenamento. A conta de armazenamento resultante é denominada storage2 .
No entanto, se você executar uma implantação chamada newStorage que implanta uma conta de armazenamento denominada storage1 e imediatamente após a conclusão da execução de outra implantação chamada newStorage que implanta uma conta de armazenamento denominada storage2 , você tem duas contas de armazenamento. Um é chamado storage1 , e o outro é nomeado storage2 . Mas, você tem apenas uma entrada no histórico de implantação.
Ao especificar um nome exclusivo para cada implantação, você pode executá-los simultaneamente sem conflitos. Se você executar uma implantação chamada newStorage1 que implanta uma conta de armazenamento denominada storage1 e, ao mesmo tempo, executar outra implantação chamada newStorage2 que implanta uma conta de armazenamento denominada storage2 , você tem duas contas de armazenamento e duas entradas no histórico de implantação.
Para evitar conflitos com implantações simultâneas e para garantir entradas exclusivas no histórico de implantação, dê a cada implantação um nome exclusivo.
Implantar especificação de modelo
Em vez de implantar um modelo local ou remoto, você pode criar uma especificação de modelo. A especificação do modelo é um recurso em sua assinatura do Azure que contém um modelo do ARM. Ele facilita o compartilhamento seguro do modelo com usuários em sua organização. Use o controle de acesso baseado em função do Azure (RBAC do Azure) para conceder acesso à especificação do modelo. Este recurso está atualmente em visualização.
Os exemplos a seguir mostram como criar e implantar uma especificação de modelo. Esses comandos só estarão disponíveis se você tiver se inscrito na versão prévia.
Primeiro, crie a especificação do modelo fornecendo o modelo ARM.
Azure PowerShell

Copiar
New-AzTemplateSpec `
  -Name storageSpec `
  -Version 1.0 `
  -ResourceGroupName templateSpecsRg `
  -Location westus2 `
  -TemplateJsonFile ./mainTemplate.json
Em seguida, obtenha a ID da especificação do modelo e implante-a.
Azure PowerShell

Copiar
$id = (Get-AzTemplateSpec -Name storageSpec -ResourceGroupName templateSpecsRg -Version 1.0).Version.Id

New-AzResourceGroupDeployment `
  -ResourceGroupName demoRG `
  -TemplateSpecId $id
Para obter mais informações, consulte Azure Resource Manager de especificações de modelo (versão prévia).
Visualizar alterações
Antes de implantar seu modelo, você pode visualizar as alterações que o modelo fará no seu ambiente. Use a operação What-If para verificar se o modelo faz as alterações que você espera. O What-If também valida o modelo para erros.
Passar valores de parâmetro
Para passar valores de parâmetros, você pode usar parâmetros inline ou um arquivo de parâmetros.
Parâmetros embutidos
Para passar parâmetros inline, forneça os nomes do parâmetro com o comando New-AzResourceGroupDeployment. Por exemplo, para passar uma string e array para um template, use:
PowerShell

Copiar
$arrayParam = "value1", "value2"
New-AzResourceGroupDeployment -ResourceGroupName testgroup `
  -TemplateFile c:\MyTemplates\demotemplate.json `
  -exampleString "inline string" `
  -exampleArray $arrayParam
Você também pode obter o conteúdo do arquivo e fornecer esse conteúdo como um parâmetro embutido.
PowerShell

Copiar
$arrayParam = "value1", "value2"
New-AzResourceGroupDeployment -ResourceGroupName testgroup `
  -TemplateFile c:\MyTemplates\demotemplate.json `
  -exampleString $(Get-Content -Path c:\MyTemplates\stringcontent.txt -Raw) `
  -exampleArray $arrayParam
Obtendo um valor de parâmetro de um arquivo é útil quando você precisa fornecer valores de configuração. Por exemplo, você pode fornecer valores de cloud-init para uma máquina virtual Linux.
Se você precisar passar uma matriz de objetos, crie tabelas de hash no PowerShell e adicione-as a uma matriz. Passe essa matriz como um parâmetro durante a implantação.
PowerShell

Copiar
$hash1 = @{ Name = "firstSubnet"; AddressPrefix = "10.0.0.0/24"}
$hash2 = @{ Name = "secondSubnet"; AddressPrefix = "10.0.1.0/24"}
$subnetArray = $hash1, $hash2
New-AzResourceGroupDeployment -ResourceGroupName testgroup `
  -TemplateFile c:\MyTemplates\demotemplate.json `
  -exampleArray $subnetArray
Arquivos de parâmetros
Em vez de passar parâmetros como valores embutidos no script, talvez seja mais fácil usar um arquivo JSON que contenha os valores de parâmetro. O arquivo de parâmetro pode ser um arquivo local ou um arquivo externo com um URI acessível.
Para saber mais sobre o arquivo de parâmetro, confira Criar arquivo de parâmetro do Resource Manager.
Para passar um arquivo de parâmetro local, use o TemplateParameterFile parâmetro:
PowerShell

Copiar
New-AzResourceGroupDeployment -Name ExampleDeployment -ResourceGroupName ExampleResourceGroup `
  -TemplateFile c:\MyTemplates\azuredeploy.json `
  -TemplateParameterFile c:\MyTemplates\storage.parameters.json
Para passar um arquivo de parâmetro externo, use o TemplateParameterUri parâmetro:
PowerShell

Copiar
New-AzResourceGroupDeployment -Name ExampleDeployment -ResourceGroupName ExampleResourceGroup `
  -TemplateUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-storage-account-create/azuredeploy.json `
  -TemplateParameterUri https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/101-storage-account-create/azuredeploy.parameters.json











New-AzResourceGroupDeployment -ResourceGroupName <resource-group-name>
 -TemplateFile <path-to-template>
Para implantar em uma assinatura, use
 New-AzSubscriptionDeployment , que é um alias do
  New-AzDeployment cmdlet:
Azure PowerShell










# Azure Machine Learning Lab Exercises

This repository contains the hands-on lab exercises for Microsoft course [DP-100 *Designing and Implementing a Data Science Solution on Azure*](https://docs.microsoft.com/learn/certifications/courses/dp-100t01) and the equals to [self-paced modules on Microsoft Learn](https://docs.microsoft.com/learn/paths/build-ai-solutions-with-azure-ml-service/). The labs are designed to accompany the learning materials and enable you to practice using the technologies described them.

You can view the instructions for the lab exercises at **[https://aka.ms/mslearn-dp100](https://aka.ms/mslearn-dp100)**.

## What are we doing?

- To support this course, we will need to make frequent updates to the course content to keep it current with the Azure services used in the course.  We are publishing the lab instructions and lab files on GitHub to keep the content current with changes in the Azure platform.

- We hope that this brings a sense of collaboration to the labs like we've never had before - when Azure changes and you find it first during a live delivery, go ahead and submit a pull-request to update the lab content.  Help your fellow MCTs.

## How should I use these files relative to the released MOC files?

- The instructor guide and PowerPoints are still going to be your primary source for teaching the course content.

- These files on GitHub are designed to be used in the course labs.

- It will be recommended that for every delivery, trainers check GitHub for any changes that may have been made to support the latest Azure services.

## What about changes to the student handbook?

- We will review the student handbook on a quarterly basis and update through the normal MOC release channels as needed.

## How do I contribute?

- Any MCT can submit a pull request to the code or content in the GitHub repo, Microsoft and the course author will triage and include content and lab code changes as needed.

- If you have suggestions or spot any errors, please report them as [issues](https://github.com/MicrosoftLearning/mslearn-dp100/issues).

## Notes

### Classroom Materials

The labs are provided in this GitHub repo rather than in the student materials in order to (a.) share them with other learning modalities, and (b.) ensure that the latest version of the lab files is always used in classroom deliveries. This approach reflects the nature of an always-changing cloud-based interface and platform.

Anyone can access the files in this repo, but Microsoft Learning support is limited to MCTs teaching this course only.
