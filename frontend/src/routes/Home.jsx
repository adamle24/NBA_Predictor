import { useState } from "react";
import PredictSection from "../components/PredictSection";
import PlayerDataSection from "../components/PlayerDataSection";
import { Box, Container } from "@mui/material";


function Home() {
    const [homeTeam, setHomeTeam] = useState(null);
    const [awayTeam, setAwayTeam] = useState(null);

    return (
        <Box>
            <PredictSection
                homeTeam={homeTeam}
                setHomeTeam={setHomeTeam}
                awayTeam={awayTeam}
                setAwayTeam={setAwayTeam}    
            />
            <PlayerDataSection homeTeam={homeTeam} awayTeam={awayTeam}/>
        </Box>
    );
}

export default Home;