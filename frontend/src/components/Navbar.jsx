import logo from "../assets/logo_1.png";
import { AppBar, Toolbar, Typography, Button, Container, Box } from "@mui/material";
import { Link } from "react-router-dom";

function Navbar() {
    const linkStyle = {
        textDecoration: "none",
        color: "primary.main",
        "&:visited": { color: "primary.main" },

        "&:hover": { 
            color: "#03a9f4",
            padding: "6px 12px",
         },

        "&:focus-visible": {
            outline: `3px solid #1976d2`,
            outlineOffset: 2,
            borderRadius: 8,
        }
    };

    return (
        <AppBar 
        osition="sticky" 
        elevation={0} 
        sx={{ 
            backgroundColor: "transparent",
            backdropFilter: "blur(10px)",
            borderBottom: "1px solid #e0e0e0",    
        }}>
            <Container maxWidth="lg">
                <Toolbar disableGutters sx={{ gap: 2}}>
                    <Box
                        component={Link} 
                        to="/"
                        sx= {{
                            display: "flex",
                            alignItems: "center",
                            gap: 1,
                            ...linkStyle,
                        }}
                    >
                    <Box
                        component="img"
                        src={logo}
                        sx= {{
                            height: { xs: 32, sm: 40, md: 48},
                            width: "auto",
                        }}
                    />

                    <Typography  variant="h6" sx={{ fontWeight: 700 }}>
                        NBA Predictor
                    </Typography>

                    </Box>
                    
                    <Box sx={{ flexGrow: 1 }}/>
                    {/*
                    <Typography
                        component={Link}
                        to="/teams"
                        sx={{
                            fontWeight: 500,
                            ...linkStyle, 
                        }}
                        >
                            Teams
                    </Typography> 
                    */}

                </Toolbar>
            </Container>
        </AppBar>
    );
}


export default Navbar;