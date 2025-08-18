import StatSection from "./StatSection";
import { Box, Typography, Grid, Container } from "@mui/material";

function normalizeAbbreviation(abb) {
    const map = {
        bkn: "brk",
        cha: "cho",
        phx: "pho",
    };
    return map[abb] || abb;
}

function PlayerDataSection( {homeTeam, awayTeam} ) {
    return(
        <Box sx={{
            backgroundImage: "linear-gradient(to bottom, #83bdf3ff, #ffffffff)",
        }}>
            <Grid container sx={{
                justifyContent: "space-around",
            }}>
                <Container maxWidth="lg">
                    <Grid container justifyContent="space-between">
                        {homeTeam && (
                            <Grid>
                                <Box sx={{  p: 2 }}>
                                    <Typography variant="h5">{homeTeam.label} Top Performer in:</Typography>
                                    <StatSection teamAbbreviation={normalizeAbbreviation(homeTeam.value)}/>
                                </Box>

                            </Grid>
                        )}

                        {awayTeam && (
                            <Grid>
                                <Box sx={{ p: 2, alignItems: "center" }}>
                                    <Typography variant="h5">{awayTeam.label} Top Performer in:</Typography>
                                    <StatSection teamAbbreviation={normalizeAbbreviation(awayTeam.value)}/>
                                </Box>

                            </Grid>
                        )}

                    </Grid>
                    
                </Container>
            </Grid>
        </Box>
    );
}

export default PlayerDataSection;