export async function getRecentPrediction(homeTeam, awayTeam) {
    try {
        const url = `http://127.0.0.1:8000/recentpredict/${homeTeam.value}-${awayTeam.value}`;
        const response = await fetch(url, {
            method: "GET",
        });

        if (!response.ok) {
            throw new Error("HTTP error");
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function getPrediction(homeTeam, awayTeam) {
    try {
        const url = `http://127.0.0.1:8000/predict/${homeTeam.value}-${awayTeam.value}`;
        const response = await fetch(url, {
            method: "GET",
        });

        if (!response.ok) {
            throw new Error("HTTP error");
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function getTeamLeaders(TeamAbbreviation) {
    try {
        const url=`http://127.0.0.1:8000/team/leaders/${TeamAbbreviation}`;
        const response = await fetch(url, {
            method: "GET",
        });

        const data = await response.json();
        return data;

    } catch (error) {
        console.error(error);
        throw error;
    }
}
