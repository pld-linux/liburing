Summary:	Linux-native io_uring I/O access library
Summary(pl.UTF-8):	Biblioteka natywnego dla Linuksa dostępu we/wy io_uring
Name:		liburing
Version:	2.13
Release:	1
License:	LGPL v2+ or MIT
Group:		Libraries
Source0:	https://brick.kernel.dk/snaps/%{name}-%{version}.tar.bz2
# Source0-md5:	479b8a15948dee9e6fd91052e78e788f
URL:		https://git.kernel.dk/cgit/liburing/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer -fno-stack-protector
%define		filterout_c	-fstack-protector.*

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%description -l pl.UTF-8
Biblioteka udostępnia w sposób szybki i wydajny natywne,
asynchroniczne operacje we/wy dla jądra Linuksa, zarówno buforowane,
jak i O_DIRECT.

%package devel
Summary:	Header files and development documentation for liburing
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja programistyczna do biblioteki liburing
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for Linux-native io_uring I/O access library.

%description devel -l pl.UTF-8
Pliki nagłówkowe do biblioteki dostępu do natywnego dla Linuksa we/wy
io_uring.

%package static
Summary:	Static liburing library
Summary(pl.UTF-8):	Statyczna biblioteka liburing
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static liburing library.

%description static -l pl.UTF-8
Statyczna biblioteka liburing.

%package ffi
Summary:	io_uring FFI library
Summary(pl.UTF-8):	Biblioteka FFI dla io_uring
Group:		Libraries

%description ffi
io_uring FFI library.

%description ffi -l pl.UTF-8
Biblioteka FFI dla io_uring.

%package ffi-devel
Summary:	Development files for liburing-ffi
Summary(pl.UTF-8):	Pliki programistyczne do biblioteki liburing-ffi
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-ffi = %{version}-%{release}

%description ffi-devel
Development files for liburing-ffi.

%description ffi-devel -l pl.UTF-8
Pliki programistyczne do biblioteki liburing-ffi.

%package ffi-static
Summary:	Static liburing-ffi library
Summary(pl.UTF-8):	Statyczna biblioteka liburing-ffi
Group:		Development/Libraries
Requires:	%{name}-ffi-devel = %{version}-%{release}

%description ffi-static
Static liburing-ffi library.

%description ffi-static -l pl.UTF-8
Statyczna biblioteka liburing-ffi.

%prep
%setup -q

%build
# not autoconf configure
./configure \
	--cc="%{__cc}" \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libdevdir=%{_libdir} \
	--mandir=%{_mandir} \
	--includedir=%{_includedir}

%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	V=1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post   ffi -p /sbin/ldconfig
%postun ffi -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/liburing.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liburing.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liburing.so
%{_includedir}/liburing
%{_includedir}/liburing.h
%{_pkgconfigdir}/liburing.pc
%{_mandir}/man2/io_uring_*.2*
%{_mandir}/man3/__io_uring_*.3*
%{_mandir}/man3/IO_URING_*.3*
%{_mandir}/man3/io_uring_*.3*
%{_mandir}/man7/io_uring.7*

%files static
%defattr(644,root,root,755)
%{_libdir}/liburing.a

%files ffi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liburing-ffi.so.*.*
%attr(755,root,root) %ghost %{_libdir}/liburing-ffi.so.2

%files ffi-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liburing-ffi.so
%{_pkgconfigdir}/liburing-ffi.pc

%files ffi-static
%defattr(644,root,root,755)
%{_libdir}/liburing-ffi.a
