source("modules/UiUtils/dynamicDropdown.R")
source("modules/Visualization/customPlot.R")


server <- function(input, output, session) {


  # a reactive event updates the app when it occurs
  d <- eventReactive(input$fileUpload, {
      # read the csv upload
      df <- read.csv(input$fileUpload$datapath)
      # create fake cohorts
      df$cohort <- paste("c", sample(1:250, nrow(df), replace = TRUE), sep = "")
      df
    }
  )


  ### manage clicks ------------------------------------------------------------
  # this saves clicks to avoids double refreshes
  savedClicks <- reactiveValues(click = NULL, pcaClick = NULL, pcaClick2 = NULL)

  # this uses the click to select the data in it
  highlighted <- observeEvent(input$mainBrush, {
    savedClicks$click <- brushedPoints(d(), input$mainBrush)
  })

  # this uses the click to select the data in it
  pcaHighlighted <- observeEvent(input$pcaBrush, {
    savedClicks$pcaClick <- brushedPoints(pcaWithLabels(), input$pcaBrush)
  })

  pcaHighlighted2 <- observeEvent(input$pcaBrush2, {
    savedClicks$pcaClick2 <- brushedPoints(pcaWithLabels(), input$pcaBrush2)
  })


  ##### main plot --------------------------------------------------------------
  # create the dropdowns
  output$yOptions <- dynamicDropdown(d(), inputId = "xAxisSelected",
                                     label = "x-Axis", selected = "texture_mean")

  output$xOptions <- dynamicDropdown(d(), inputId = "yAxisSelected",
                                     label = "Y-Axis", selected = "radius_mean")
  # create the large, main plot
  scatterReactive <- reactive({

    # wait for input
    req(input$xAxisSelected)
    req(input$yAxisSelected)

    toLabel <- sort(as.factor(savedClicks$click$cohort))

    customPlot(df = d(),
               xString = input$xAxisSelected,
               yString = input$yAxisSelected,
               toLabel = toLabel) +
               theme(
                 legend.title = element_text(color = "black", size = 30),
                 legend.text = element_text(size = 30)
               ) +
               theme(legend.text = element_text(size = 10)) +
                     theme(legend.title = element_blank())
  })



  ##### tiled plots ------------------------------------------------------------


  ### plot 1
  # create its dropdowns
  output$plot1X <- dynamicDropdown(d(), inputId = "miniDropdown1XSelected",
                                   label = "X-Axis", selected = "texture_mean")

  output$plot1Y <- dynamicDropdown(d(), inputId = "miniDropdown1YSelected",
                                   label = "Y-Axis", selected = "radius_mean")

  scatterPlot1 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown1XSelected)
    req(input$miniDropdown1YSelected)

    # waits to hear what to label (by cohort)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    # calls the custom plot from Visualization module
    customPlot(df = d(),
               xString = input$miniDropdown1XSelected,
               yString = input$miniDropdown1YSelected,
               toLabel = toLabel)
  })


  ### plot 2
  # create its dropdowns
  output$plot2X <- dynamicDropdown(d(), inputId = "miniDropdown2XSelected",
                                   label = "X-Axis", selected = "perimeter_mean")

  output$plot2Y <- dynamicDropdown(d(), inputId = "miniDropdown2YSelected",
                                   label = "Y-Axis", selected = "radius_mean")

  scatterPlot2 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown2XSelected)
    req(input$miniDropdown2YSelected)

    # waits to hear what to label (by subject)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    # calls the custom plot from Visualization module
    customPlot(df = d(),
               xString = input$miniDropdown2XSelected,
               yString = input$miniDropdown2YSelected,
               toLabel = toLabel)
  })


  ### plot 3
  # create its dropdowns
  output$plot3X <- dynamicDropdown(d(), inputId = "miniDropdown3XSelected",
                                    label = "X-Axis", selected= "area_mean")
  output$plot3Y <- dynamicDropdown(d(), inputId = "miniDropdown3YSelected",
                                    label = "Y-Axis", selected = "radius_mean")

  # create the plot
  scatterPlot3 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown3XSelected)
    req(input$miniDropdown3YSelected)

    # waits to hear what to label (by cohort)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    # calls the custom plot from Visualization module
    customPlot(df = d(),
               xString = input$miniDropdown3XSelected,
               yString = input$miniDropdown3YSelected,
               toLabel = toLabel)
  })


  ### plot 4
  # create its dropdowns
  output$plot4X <- dynamicDropdown(d(), inputId = "miniDropdown4XSelected",
                                   label = "X-Axis", selected = "smoothness_mean")
  output$plot4Y <- dynamicDropdown(d(), inputId = "miniDropdown4YSelected",
                                    label = "Y-Axis", selected = "radius_mean")

  # create the plot
  scatterPlot4 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown4XSelected)
    req(input$miniDropdown4YSelected)

    # waits to hear what to label (by cohort)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    # calls the custom plot from Visualization module
    customPlot(df = d(),
               xString = input$miniDropdown4XSelected,
               yString = input$miniDropdown4YSelected,
               toLabel = toLabel)
  })


  ### plot 5
  # create its dropdowns
  output$plot5X <- dynamicDropdown(d(), inputId = "miniDropdown5XSelected",
                                   label = "X-Axis", selected = "compactness_mean")
  output$plot5Y <- dynamicDropdown(d(), inputId = "miniDropdown5YSelected",
                                   label = "Y-Axis", selected = "radius_mean")
  scatterPlot5 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown5XSelected)
    req(input$miniDropdown5YSelected)

    # waits to hear what to label (by cohort)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    customPlot(df = d(),
               xString = input$miniDropdown5XSelected,
               yString = input$miniDropdown5YSelected,
               toLabel = toLabel)
  })


  ### plot 6
  # create its dropdowns
  output$plot6X <- dynamicDropdown(d(), inputId = "miniDropdown6XSelected",
                                   label = "X-Axis", selected = "concavity_mean")
  output$plot6Y <- dynamicDropdown(d(), inputId = "miniDropdown6YSelected",
                                   label = "Y-Axis", selected = "radius_mean")
  scatterPlot6 <- reactive({

    # wait for data - avoids flash of a red error message
    req(input$miniDropdown6XSelected)
    req(input$miniDropdown6YSelected)

    # waits to hear what to label (by cohort)
    toLabel <- sort(as.factor(savedClicks$click$cohort))

    customPlot(df = d(),
               xString = input$miniDropdown6XSelected,
               yString = input$miniDropdown6YSelected,
               toLabel = toLabel)
  })




  ### render the outputs -------------------------------------------------------

  # the main, large plot
  output$scatterInteractive <- renderPlot(scatterReactive(),
                                          height = 1200, width = 1400)

  output$current <- renderTable(d()[savedClicks$click$cohort, c("Subject")])

  # each of the small tiled plots
  output$tiledScatter1 <- renderPlot(scatterPlot1(), height = 450, width = 700)
  output$tiledScatter2 <- renderPlot(scatterPlot2(), height = 450, width = 700)
  output$tiledScatter3 <- renderPlot(scatterPlot3(), height = 450, width = 700)
  output$tiledScatter4 <- renderPlot(scatterPlot4(), height = 450, width = 700)
  output$tiledScatter5 <- renderPlot(scatterPlot5(), height = 450, width = 700)
  output$tiledScatter6 <- renderPlot(scatterPlot6(), height = 450, width = 700)

  output$dfView <- renderTable(d())

}
