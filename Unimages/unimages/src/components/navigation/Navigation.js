import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';

export function Navigation() {
    return (
        <>
            <Navbar bg="primary" variant="dark">
                <Container>
                    <Navbar.Brand href="/">Unimages</Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <Nav.Link href="/about">Sobre</Nav.Link>
                        <Nav.Link href="/profile">Perfil</Nav.Link>
                        <Nav.Link href="/contact">Contatos</Nav.Link>
                    </Nav>
                </Container>
            </Navbar>
        </>
    );
}