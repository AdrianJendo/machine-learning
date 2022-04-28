import React from "react";
import Card from "@mui/material/Card";
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";

function NotFound() {
    return (
        <>
            <Box minHeight="5vh" />
            <Card
                sx={{
                    height: "60vh",
                    p: 2,
                    mx: { xs: 2, lg: 3 },
                    mt: 8,
                    mb: 8,
                }}
            >
                <Box
                    height="100%"
                    display="flex"
                    flexDirection="column"
                    justifyContent="center"
                    alignItems="center"
                >
                    <Typography variant="h1">404</Typography>
                    <Typography variant="h3">
                        <i>URL not found</i>
                    </Typography>
                </Box>
            </Card>
        </>
    );
}

export default NotFound;
