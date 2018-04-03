getArOne <- function(N=1000, phi=0.4) {
    Z = rnorm(N, 0, 1)
    X = NULL
    X[1] = Z[1]
    for (t in 2:N) {
        X[t] = Z[t] + phi * X[t - 1]
    }
    return(ts(X))
}

getArP <- function(coeffs, N=1000) {
    return(arima.sim(list(ar=coeffs), n=N))
}

visualizeArProcess <- function(X, title="AR(p) Time Series on White Noise") {
    par(mfrow=c(2,1))
    plot(X, main=title)
    return(acf(X, main=title))
}

partialAcf <- function(phis, N=1000) {
    data.ts = arima.sim(n=N, list(ar=phis))
    title = getProcessTitle(phis)
    par(mfrow=c(3, 1))
    plot(data.ts, main=title)
    acf(data.ts, main='Autocorrelation')
    acf(data.ts, type='partial', main='Partial Autocorrelation')
}

getProcessTitle <- function(phis) {
    nPhis = length(phis)
    titleItems <- vector('list', 2 * nPhis)
    titleItems[1] = 'Autoregressive Process with phi1='
    titleItems[2] = phis[1]
    for (i in 2:nPhis) {
        titleItems[2 * i - 1] = paste(', phi', i, '=', sep='')
        titleItems[2 * i] = phis[i]
    }
    return(do.call('paste', c(titleItems, sep='')))
}

