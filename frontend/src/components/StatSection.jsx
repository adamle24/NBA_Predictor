import { useState } from "react";
import { useEffect } from "react";
import { getTeamLeaders } from "../services/api";
import PlayerCard from "./PlayerCard";
import { Card, CardContent, ToggleButtonGroup, ToggleButton, Box} from "@mui/material";

function StatSection( {teamAbbreviation, defaultStat = "PTS" } ) {

    const stat_cats = ["PTS", "AST", "REB", "STL", "BLK", "3PT"];
    const [leaders, setLeaders] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [stat, setStat] = useState( stat_cats.includes(defaultStat) ? defaultStat: "PTS");

    useEffect(() => {
        let ignore = false;


        (async () => {
            try {
                setLeaders(null);
                setLoading(true);
                
                const data = await getTeamLeaders(teamAbbreviation);
                if (!ignore) {
                    setLeaders(data);
                    setLoading(false);
                }

            } catch (error) {
                if (!ignore) setError("Failed to load leaders");
            } finally {
                if (!ignore) setLoading(false);
            }
        })();
        return () => {
            ignore = true;
        }
    }, [teamAbbreviation]);

    return(
        <Card> 
            <Box sx={{ display: "flex", justifyContent: "center" }}>
                <CardContent>
                    {/* Select the stat */}
                    <ToggleButtonGroup
                        value={stat}
                        exclusive
                        onChange={(_, next) => next && setStat(next)}
                    >
                        {stat_cats.map((s) => (
                            <ToggleButton key={s} value={s} sx={{ 
                                border: "1px solid blue",
                                borderColor: "black",
                                color: "white",
                                backgroundColor: "primary.main",
                                "&.Mui-selected": {
                                    backgroundColor: "grey"
                                    }
                                }}>
                                {s}
                            </ToggleButton>
                        ))}
                    </ToggleButtonGroup>

                    {/* Display players */}
                    {leaders && (
                        <Box sx={{ display: "flex", justifyContent: "center" }}>
                            <PlayerCard
                                statName={stat === "PTS" ? "PTS" : stat}
                                player={leaders[stat]}
                            />
                        </Box>
                    )}
                </CardContent>
            </Box>
        </Card>
    );
};

export default StatSection;