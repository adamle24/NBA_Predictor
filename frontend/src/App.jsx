import { ThemeProvider, CssBaseline, createTheme } from "@mui/material";
import { BrowserRouter, Routes, Route, Navigate, Link } from "react-router-dom";
import Navbar from './components/Navbar';
import Home from "./routes/Home";
import Teams from "./routes/Teams";

const theme = createTheme({
  palette: {
    mode: "light",
    primary: { main: "#1E88E5" },
    secondary: { main: "#ffffffff" },
  },

  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial"'
  },

  shape: { borderRadius: 16},
  
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          padding: "12px 24px",
        },
        containedPrimary: {
          "&:hover": {
            backgroundColor: "#1565C0",
          }
        },
      },
    },

    MuiCard: {},

    MuiAppBar: {
      styleOverrides: {
        root: {
          backgroundColor: "#212121",
        },
      },
    }
  },

});

function App() {

  return (

    <ThemeProvider theme={theme}>
      <CssBaseline />
        <BrowserRouter>
          <Navbar />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/teams" element={<Teams />} />
          </Routes>
      </BrowserRouter>
    </ThemeProvider>
  )
}

export default App;
