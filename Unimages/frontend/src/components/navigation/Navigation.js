import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';

export function Navigation() {
    return (
        <>
            <Navbar bg="primary" variant="dark">
                <Container>
                    <Navbar.Brand href="/">Unimages</Navbar.Brand>
                    <Nav className="me-auto">
                        <Nav.Link href="/">Home</Nav.Link>
                        <NavDropdown title="Imagens" id="basic-nav-dropdown">
                            <NavDropdown.Item href="#action/3.1">Fotos</NavDropdown.Item>
                            <NavDropdown.Item href="#action/3.2">Ilustrações</NavDropdown.Item>
                            <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
                            <NavDropdown.Divider />
                            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
                        </NavDropdown>
                        <Nav.Link href="/about">Sobre</Nav.Link>
                        <Nav.Link href="/profile">Perfil</Nav.Link>
                        <Nav.Link href="/contact">Contatos</Nav.Link>
                    </Nav>
                </Container>
            </Navbar>
        </>
    );
}