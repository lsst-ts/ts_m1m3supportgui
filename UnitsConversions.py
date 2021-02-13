import astropy.units as u

__all__ = ["M2MM", "R2ARCSEC", "MM2M", "ARCSEC2R"]

M2MM = (1 * u.m).to(u.mm).value
R2ARCSEC = (1 * u.rad).to(u.arcsec).value

MM2M = 1 / M2MM
ARCSEC2R = 1 / R2ARCSEC
