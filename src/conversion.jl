# ========================================================================================
# File: conversion.jl
# Brief: Code for converting from cartestian state to Keplerian elements
# Author: Rolfe Power <rpower@purdue.edu>
# ========================================================================================

using CSV
using DataFrames

include("path_utils.jl")
include("keplerian_elements.jl")

function main()
    dataset_files = get_data_files()
    datasets = Dict()
    for (name, path) in dataset_files
        datasets[name] = 
        transform(
            DataFrame(CSV.File(path)),
            [:xh, :yh, :zh, :vxh, :vyh, :vz] => 
                ByRow(
                    (xh, yh, zh, vxh, vyh, vz) -> KeplerianElements(gm, [xh, yh, zh, vxh, vyh, vz])
                ) => :ke
        )
    end
    return datasets
end
