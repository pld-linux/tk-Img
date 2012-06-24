Summary:	Additional file formats support for Tk.
Name:		tk-Img
Version:	1.2.4
Release:	1
License:	distributable
Group:		Development/Languages/Tcl
Source0:	http://ftp.neosoft.com/cl/sorted/packages-8.0/graphics/%{name}/%{version}/img%{version}.tar.gz
Patch0:		%{name}-DESTDIR.patch
URL:		http://members1.chello.nl/~j.nijtmans/img.html
BuildRequires:	tk-devel
BuildRequires:	zlib-devel >= 1.1.3
BuildRequires:	libpng-devel >= 1.0.8
BuildRequires:	libjpeg-devel >= 6b
BuildRequires:	libtiff-devel >= 3.5.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package enhances Tk, adding support for many other Image formats:
BMP, XBM, XPM, GIF (with transparency, but without LZW), PNG, JPEG,
TIFF and postscript.

%prep
%setup -qn img%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE README changes license.terms
%{_libdir}/Img*
