library(ggplot2)

customPlot <- function(df, xString, yString, toLabel)
{
  # custom colot scheme
  colors <- c("M" = "#2E8B57", "B" = "#4B0082")
  # create a plot with desired columns
  ggplot(df,
    aes_string(xString, yString)) +
      # color them by diagnosis
      geom_point(aes(colour = diagnosis), size = 8, alpha = 0.55) +
      # label the selected regions by cohort, if there are selections
      geom_text(
        aes(label = ifelse(cohort %in% toLabel, as.character(cohort), "")),
            size = 8, vjust = "inward", hjust = "inward", color = "orange") +
      # set font size, etc
      theme(legend.text = element_text(size = 10, color = "black")) +
      theme(legend.title = element_blank()) +
      # color schem3
      scale_color_manual(values = colors)

}
