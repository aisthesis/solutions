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

