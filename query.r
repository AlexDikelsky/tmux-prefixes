df = read.csv("responses.csv")
con <- file('results.log')
sink(con, append=TRUE)
sink(con, append=TRUE, type="message")
for (i in levels) {
    cat(nrow(df[which(df$keys == i),]))
    cat(",", i, "\n")
}
sink()
sink(type="message")
cat(readLines("results.log"), sep="\n")
