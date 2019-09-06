library(shiny)

# will make a dynamic selectize dropdown in 1 line
# save me Superman, from boilerplate hell
dynamicDropdown <- function(df, inputId, label, selected = "PB_VCN_M3")
{
  renderUI({
    selectizeInput(inputId = inputId, label = label,
      choices = sort(colnames(df)),
      multiple = FALSE,
      selected = selected
    )
  })
}
