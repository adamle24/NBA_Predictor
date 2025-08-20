function normalizeAbbreviation(abb) {
    const map = {
        bkn: "brk",
        cha: "cho",
        phx: "pho",
    };
    return map[abb] || abb;
}

export default normalizeAbbreviation;