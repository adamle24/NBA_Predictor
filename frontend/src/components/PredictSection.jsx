import TeamSelector from "./TeamSelector";
import { useState } from "react";
import { getPrediction } from "../services/api";
import { getFullTeamName } from "../utils/teamUtils";
import { Box, Typography, Button, Grid, Stack, Container, Paper} from "@mui/material";

function PredictSection( {homeTeam, setHomeTeam, awayTeam, setAwayTeam} ) {

    const [isLoading, setIsLoading] = useState(false);
    const [prediction, setPrediction] = useState(null);
    const [error, setError] = useState(null);
    
    const handlePredictClick = async () => {
        if (!homeTeam || !awayTeam) {
            setError("Select the home team and away team");
            return;
        }

        setIsLoading(true);
        setError(null);
        setPrediction(null);

        try {
            const result = await getPrediction(homeTeam, awayTeam);
            setPrediction(result);
        } catch (error) {
            setError("failed to get prediction");
        } finally {
            setIsLoading(false);
        }
    }

  return (
        <Box 
            sx={{ 
                borderBottom: "1px solid #e0e0e0"
                
            }}>
            
            <Container maxWidth="lg">
            {/* Team selector*/}
                <Grid 
                    container
                    sx={{ 
                        mt: 8,
                        alignItems: "center",
                    }}>
                    <Grid item>
                        <Box sx={{ p: 4 }}>
                            <Stack spacing={3}>
                                <Typography variant="h3">Choose two teams!</Typography>
                                <Box sx={{ maxWidth: 500}}>
                                    <Typography variant="body2">A prediction will be made using features deemed most important by a logistic regression model trained on historical NBA data from the 1970s to the 2024 NBA season. </Typography>
                                </Box>
                                <Stack direction={{sm: "column", md: "row" }} spacing={6} justifyContent="flex-start" alignItems="flex-start">
                                    <Stack alignItems="flex-start">
                                        <Typography variant="h5">Home Team</Typography>

                                        {homeTeam && (
                                            <Box 
                                                component="img"
                                                src={`/team-logos/${homeTeam.value}.png`}
                                                alt={homeTeam.value}
                                                sx={{ height: 55, width: "auto", mt: 3, alignSelf: "center"}}
                                            />
                                        )}

                                        <TeamSelector 
                                            name="home-team" 
                                            onTeamChange={(team) => {
                                                setHomeTeam(team);
                                                setPrediction(null);
                                                setError(null);
                                            }}
                                        />
                                    </Stack>

                                    <Stack alignItems="flex-start">
                                        <Typography variant="h5">Away Team</Typography>

                                        {awayTeam && (
                                            <Box 
                                                component="img"
                                                src={`/team-logos/${awayTeam.value}.png`}
                                                alt={awayTeam.value}
                                                sx={{ height: 55, width: "auto", mt: 3, alignSelf: "center"}}
                                            />
                                        )}

                                        <TeamSelector 
                                            name="away-team" 
                                            onTeamChange={(team) => {
                                                setAwayTeam(team);
                                                setPrediction(null);
                                                setError(null);
                                            }}
                                        />
                                    </Stack>

                                </Stack>

                                <Button
                                    variant="contained"
                                    color="primary"
                                    onClick={handlePredictClick}
                                    disabled={isLoading || !homeTeam || !awayTeam}
                                    sx={{ maxWidth: 450}}
                                >
                                    Predict
                                </Button>
                            </Stack>
                        </Box>
                    </Grid>

                    
                    {/* Display the winner */}

                    <Grid 
                        xs={12} 
                        md="auto"
                        sx={{
                            ml: {md: "auto" },
                        }}
                    >
                        <Paper
                            variant="outlined"   
                            sx={{
                                p: 4,
                                width: 450,
                                minHeight: 420,
                                display: "flex",
                                alignItems: "center",
                                justifyContent: "center",
                            }} 
                        >
                            {!prediction ? (
                                <Typography variant="body">No prediction made, select two teams and click on the predict button!</Typography>
                            ) : (
                                <Stack>
                                    <Typography variant="h5">The winner is...</Typography>
                                    <Typography variant="h4">{prediction.predicted_winner ? getFullTeamName(prediction.predicted_winner) : "N/A"}</Typography>
                                    <Box 
                                        component="img"
                                        src={`/team-logos/${prediction.predicted_winner.toLowerCase()}.png`}
                                        alt={prediction.predicted_winner}
                                        sx={{ height: {xs: "8rem", md:"20rem"}, width: "auto", mt: 3, alignSelf: "center"}}
                                    />
                                </Stack>
                            )}
                        </Paper>
                    </Grid>

                </Grid>

            </Container>
                
        </Box>
    );

}

export default PredictSection;