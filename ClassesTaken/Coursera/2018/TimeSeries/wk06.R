GetSarima <- function(n, D) {
    x <- NULL
    z <- rnorm(n)
    x[1:(D + 1)] <- 1
    for (i in (D + 2):n) {
        x[i] <- z[i] + 0.7 * z[i - 1] + 0.6 * z[i - D] + 0.42 * z[i - D - 1]
    }
    return(x)
}

EvalSarima <- function(data, d, D, max.p=2, max.q=2, max.P=2, max.Q=2, period=12) {
    for (p in 0:max.p) {
        for (q in 0: max.q) {
            for (P in 0:max.P) {
                for (Q in 0:max.Q) {
                    if (p + d + q + P + D + Q > 6) {
                        next
                    }
                    msg.vals <- paste(p, d, q, P, D, Q, period)
                    model <- arima(data, order=c(p, d, q), seasonal=list(order=c(P, D, Q), period=period))
                    pval <- Box.test(model$residuals, lag=log(length(model$residuals)))
                    sse <- sum(model$residuals ^ 2)
                    print(paste(msg.vals, ' : ', 'AIC=', model$aic, '  SSE=', sse, '  p-value=', pval$p.value, sep=''))
                }
            }
        }
    }
}

GetSesForecastSSEs <- function(data) {
    alpha.vals <- seq(.001, .999, by=.001)
    n.alphas <- length(alpha.vals)
    sse.tbl <- matrix(0, n.alphas, 2)
    sse.tbl[, 1] <- alpha.vals
    colnames(sse.tbl) <- c('alpha', 'sse')

    for (k in 1:n.alphas) {
        sse.tbl[k, 2] <- GetSesForecastSSE(data, alpha.vals[k])
    }
    return(sse.tbl)
}

GetSesForecastSSE <- function(data, alpha) {
    forecast.vals <- GetSesForecast(data, alpha)
    return(sum((data - forecast.vals) ^ 2))
}

GetSesForecast <- function(data, alpha) {
    n <- length(data)
    forecast.vals <- NULL
    forecast.vals[1] <- data[1]
    for (i in 2:n) {
        forecast.vals[i] <- alpha * data[i - 1] + (1 - alpha) * forecast.vals[i - 1]
    }
    return(forecast.vals)
}

GetEstForecast <- function(data, alpha, beta) {
    n <- length(data)
    forecast.vals <- NULL
    level.vals <- NULL
    trend.vals <- NULL

    forecast.vals[1] <- data[1]
    forecast.vals[2] <- data[2]
    level.vals[1] <- data[1]
    trend.vals[1] <- data[2] - data[1]

    for (i in 2:n) {
        level.vals[i] <- alpha * data[i] + (1 - alpha) * (level.vals[i - 1] + trend.vals[i - 1])
        trend.vals[i] <- beta * (level.vals[i] - level.vals[i - 1]) + (1 - beta) * trend.vals[i - 1]
        forecast.vals[i + 1] <- level.vals[i] + trend.vals[i]
    }
    return(forecast.vals)
}

AdditiveSeasonalityForecast <- function(hw.coeffs, h=1, m=12) {
    seasonal <- hw.coeffs[2 + (h %% m)]
    return(hw.coeffs['a'] + h * hw.coeffs['b'] + seasonal)
}

