export const API_BASE = import.meta.env.VITE_API_BASE_URL;

export async function getRecentPrediction(homeTeam, awayTeam) {
    try {
        const url = `${API_BASE}/recentpredict/${homeTeam.value}-${awayTeam.value}`;
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
        const url = `${API_BASE}/predict/${homeTeam.value}-${awayTeam.value}`;
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
        const url=`${API_BASE}/team/leaders/${TeamAbbreviation}`;
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
