library(shiny)
library(shinythemes)


ui <- fluidPage(
  theme = shinytheme("darkly"),
  titlePanel("StReuen"),
  sidebarLayout(
    # Sidebar panel for inputs ----
    sidebarPanel(
      h3("Please Upload a CSV"),
      # dropdown accepts CSV/Excel
      fileIn <- fileInput("fileUpload", "Select CSV file", multiple = FALSE,
                        accept = c("text/comma-separated-values,text/plain",
                                   ".csv", ".xlsx", "text/csv")
      ),
      uiOutput("yOptions"),
      uiOutput("xOptions"),
      tableOutput("current"),
      tableOutput("currentPca"),
      width = 2
    ),

    mainPanel(
      # Output: Tabset w/ plot, summary, and table ----
      tabsetPanel(type = "tabs",

        # 1st panel: the main, large main plot
        tabPanel("Main Plot",
          plotOutput("scatterInteractive",
            brush = "mainBrush"
          )
        ),

        # 2nd panel tiled display of 6 plots
        tabPanel("Selected Scatterplots",
          # first of 2 rows
          fluidRow( br(),
            column(4,
              uiOutput("plot1X"),
              uiOutput("plot1Y"),
              plotOutput("tiledScatter1",
                brush = "mainBrush"
              )
            ),
            column(4,
              uiOutput("plot2X"),
              uiOutput("plot2Y"),
              plotOutput("tiledScatter2",
                brush = "mainBrush"
              )
            ),
            column(4,
              uiOutput("plot3X"),
              uiOutput("plot3Y"),
              plotOutput("tiledScatter3",
                brush = "mainBrush"
              )
            )
          ),
          #C this could be cleaner
          br(), br(), br(), br(),
          # second of two rows
          fluidRow(
            column(4,
              uiOutput("plot4X"),
              uiOutput("plot4Y"),
              plotOutput("tiledScatter4",
                brush = "mainBrush"
              )
            ),
            column(4,
              uiOutput("plot5X"),
              uiOutput("plot5Y"),
              plotOutput("tiledScatter5",
                brush = "mainBrush"
              )
            ),
            column(4,
              uiOutput("plot6X"),
              uiOutput("plot6Y"),
              plotOutput("tiledScatter6",
                brush = "mainBrush"
              )
            )
          )
        ),
        tabPanel("View Dataset",
          br(),
          tableOutput("dfView")
        )
      )
    )
  )
)
