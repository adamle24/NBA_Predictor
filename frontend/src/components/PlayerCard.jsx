import playerPictures from "../utils/playerPictures";
import defaultPicture from "../assets/players/default.avif";
import { Card, CardMedia, CardContent, Typography, Chip, Box, Stack} from "@mui/material";

function PlayerCard({ player, statName}) {

    const { name, value, position } = player;

    const imgSrc = playerPictures[name] || defaultPicture;

    return (
        <Card sx={{
            borderRadius: 2,
            height: "100%",
        }}>
            <Box 
                sx={{
                    position: "relative",
                    width: "1",
                    aspectRatio: "4 / 3", 
                }}
            >
                <Box 
                    component="img"
                    src={imgSrc}
                    alt={name}
                    onError={() => setSrc(defaultPicture)}
                />
            </Box>

            <CardContent sx={{ textAlign: "center"}}>

                <Stack direction="row" spacing={1} alignItems="center" justifyContent="center"> 
                    <Typography variant="h6">{name}</Typography>

                    {position && (
                        <Chip 
                            size="small"
                            label={position}
                            variant="outlined"
                        />
                    )}
                </Stack>

                <Box>
                    <Typography variant="h5">{statName}: {value}</Typography>
                </Box>
            </CardContent>
        </Card>
    );
} 

export default PlayerCard;