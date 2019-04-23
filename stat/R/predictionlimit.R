""Quick and dirty prediction limits from a prediction object preds containing fitted
values and their standard errors plus an estimate of the noise levels. Combine
standard deviations in quadruture due to uncorrelated sources of noise."
predlims <- function(preds, sigma) {
    prediction.sd <- sqrt(preds$se.fit^2 + sigma^2)
    upper <- preds$fit + 2 * prediction.sd
    lower <- preds$fit - 2 * prediction.sd
    lims <- cbind(lower = lower, upper = upper)
    return(lims)
}
